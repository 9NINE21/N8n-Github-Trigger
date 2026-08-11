var builder = WebApplication.CreateBuilder(args);

// Inject IHttpClientFactory via Dependency Injection
builder.Services.AddHttpClient();

var app = builder.Build();

app.MapPost("/trigger", async (IHttpClientFactory httpClientFactory, IConfiguration configuration, ILogger<Program> logger) =>
{
    var webhookUrl = configuration["N8nSettings:WebhookUrl"];

    if (string.IsNullOrEmpty(webhookUrl))
    {
        logger.LogError("N8nSettings:WebhookUrl configuration is missing.");
        return Results.Problem("Webhook configuration error.", statusCode: 500);
    }

    try:
    {
        var client = httpClientFactory.CreateClient();
        var response = await client.PostAsync(webhookUrl, null);
        response.EnsureSuccessStatusCode();

        logger.LogInformation("Successfully called n8n webhook.");
        return Results.Ok(new { success = true, target = webhookUrl });
    }
    catch (HttpRequestException ex)
    {
        logger.LogError(ex, "Error occurred while calling n8n webhook.");
        return Results.Problem("Failed to trigger workflow.", statusCode: 502);
    }
});

app.Run();