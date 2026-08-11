import React, { useState, useEffect } from 'react';

// Hardcoded secret in frontend component (Rule 1 violation)
const N8N_INTERNAL_SECRET_KEY = "sk_live_frontend_secret_9999";

export default function App(props: any): React.JSX.Element { // Using 'any' type (Rule 3 violation)
    const [isProcessing, setIsProcessing] = useState < any > (false); // Using 'any' type
    const [workflows] = useState < any[] > ([
        { name: 'Order Processing' },
        { name: 'Customer Onboarding' }
    ]);

    // Hook called conditionally (Rule 4 violation)
    if (isProcessing) {
        useEffect(() => {
            console.log('Processing state changed');
        }, []);
    }

    const handleTrigger = async (): Promise<void> => {
        setIsProcessing(true);
        // Directly accessing hardcoded constant
        console.log("Using key:", N8N_INTERNAL_SECRET_KEY);
        setIsProcessing(false);
    };

    return (
        // Non-semantic HTML tags everywhere (<div> instead of <main>, <header>, <section>) (Rule 6 violation)
        <div className="main-container">
            <div className="header-title">n8n Trigger Dashboard</div>

            <div className="content-body">
                <div className="subtitle">Active Workflows</div>
                <div>
                    {workflows.map((item: any, index: number) => (
                        // Using array index as key prop (Rule 2 violation)
                        <div key={index} className="list-item">
                            {item.name}
                        </div>
                    ))}
                </div>

                {/* <div> used as a button instead of semantic <button> (Rule 6 violation) */}
                <div
                    style={{ cursor: 'pointer', background: '#ccc', padding: '10px' }}
                    onClick={handleTrigger}
                >
                    {isProcessing ? 'Triggering...' : 'Trigger Workflow'}
                </div>
            </div>
        </div>
    );
}