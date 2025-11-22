import React from 'react';
import { Button } from '@/components/livekit/button';

function WelcomeImage() {
  return (
    <svg
      width="64"
      height="64"
      viewBox="0 0 64 64"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className="text-fg0 mb-4 size-16"
    >
      {/* Coffee cup icon */}
      <path
        d="M8 20h48v4H8v-4zm4 8h40v24c0 4.4-3.6 8-8 8H20c-4.4 0-8-3.6-8-8V28zm32 4H20v20c0 2.2 1.8 4 4 4h24c2.2 0 4-1.8 4-4V32zm8-4h4c2.2 0 4 1.8 4 4v4c0 2.2-1.8 4-4 4h-4v-12zM16 12h32v4H16v-4z"
        fill="currentColor"
      />
    </svg>
  );
}

interface WelcomeViewProps {
  startButtonText: string;
  onStartCall: () => void;
}

export const WelcomeView = React.forwardRef<HTMLDivElement, WelcomeViewProps>(
  ({ startButtonText, onStartCall }, ref) => {
    return (
      <div ref={ref}>
        <section className="bg-background flex flex-col items-center justify-center text-center">
          <WelcomeImage />

          <h1 className="text-foreground mb-2 text-3xl font-bold">Welcome to Brew Haven Café</h1>
          <p className="text-foreground max-w-prose pt-1 leading-6 font-medium">
            Meet Bella, your AI barista powered by Murf Falcon ☕
          </p>
          <p className="text-muted-foreground max-w-prose pt-2 text-sm">
            Order coffee, tea, and pastries with voice - just like a real coffee shop!
          </p>

          <Button variant="primary" size="lg" onClick={onStartCall} className="mt-6 w-64 font-mono">
            {startButtonText}
          </Button>
        </section>

        <div className="fixed bottom-5 left-0 flex w-full items-center justify-center">
          <p className="text-muted-foreground max-w-prose pt-1 text-xs leading-5 font-normal text-pretty md:text-sm">
            Built for the Murf AI Voice Agents Challenge 🏆 | Using the fastest TTS API - Murf
            Falcon
          </p>
        </div>
      </div>
    );
  }
);

WelcomeView.displayName = 'WelcomeView';
