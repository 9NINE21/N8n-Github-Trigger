import React, { useState } from 'react';

// Strict Type Definitions
interface WorkflowItem {
    id: string;
    name: string;
}

interface TriggerButtonProps {
    onTrigger: () => Promise<void>;
    disabled: boolean;
}

// Modular Component
const TriggerButton: React.FC<TriggerButtonProps> = ({ onTrigger, disabled }) => (
    <button type="button" onClick={onTrigger} disabled={disabled}>
        {disabled ? 'Triggering...' : 'Trigger Workflow'}
    </button>
);

export default function App(): React.JSX.Element {
    const [isProcessing, setIsProcessing] = useState < boolean > (false);
    const [workflows] = useState < WorkflowItem[] > ([
        { id: 'wf_01', name: 'Order Processing' },
        { id: 'wf_02', name: 'Customer Onboarding' }
    ]);

    const handleTrigger = async (): Promise<void> => {
        setIsProcessing(true);
        const webhookUrl = import.meta.env.VITE_N8N_WEBHOOK_URL;

        try {
            if (webhookUrl) {
                await fetch(webhookUrl, { method: 'POST' });
            }
        } catch (error) {
            // Clean side-effect handling
        } finally {
            setIsProcessing(false);
        }
    };

    return (
        <main style={{ padding: '2rem' }}>
            <header>
                <h1>n8n Trigger Dashboard</h1>
            </header>
            <section>
                <h2>Active Workflows</h2>
                <ul>
                    {/* Unique list key (id instead of array index) */}
                    {workflows.map((item) => (
                        <li key={item.id}>{item.name}</li>
                    ))}
                </ul>
                <TriggerButton onTrigger={handleTrigger} disabled={isProcessing} />
            </section>
        </main>
    );
}