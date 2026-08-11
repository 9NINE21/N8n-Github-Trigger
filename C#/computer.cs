var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapPost("/trigger", (HttpContext context) =>
{
    // Hardcoded connection/config inside code (Rule 1 violation)
    string hardcodedWebhookUrl = "http://localhost:5678/webhook/live_production_key";

    // Direct instantiation with `new` instead of Dependency Injection (Rule 4 violation)
    HttpClient client = new HttpClient();

    try
    {
        // Bad C# naming style snake_case variable (Rule 2 violation)
        var post_task = client.PostAsync(hardcodedWebhookUrl, null);
        
        // Blocking .Result on async task causing deadlock potential (Rule 3 violation)
        var response = post_task.Result; 
        
        response.EnsureSuccessStatusCode();

        // Simulated EF query without .AsNoTracking() (Rule 5 violation)
        // var log = dbContext.Logs.FirstOrDefault(l => l.Id == 1); 

        return Results.Ok(new { success = true });
    }
    catch (Exception)
    {
        // Swallowing exceptions silently without logging (Rule 6 violation)
        return Results.Problem("An error occurred");
    }
});

// Non-standard method naming pascalCase / snake_case (Rule 2 violation)
void process_trigger_data()
{
    // Unused helper
}

app.Run();