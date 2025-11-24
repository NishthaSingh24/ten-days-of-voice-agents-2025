import React from 'react';
import { Button } from '@/components/livekit/button';

function WelcomeImage() {
  return (
    <div className="relative mb-6">
      {/* Glowing background circle */}
      <div className="bg-primary/20 absolute inset-0 animate-pulse rounded-full blur-3xl" />

      <svg
        width="80"
        height="80"
        viewBox="0 0 64 64"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className="text-primary relative z-10 drop-shadow-lg"
      >
        {/* Modern wellness icon - heart with pulse */}
        <path
          d="M32 54L10 32C4 26 4 16 10 10C16 4 26 4 32 10C38 4 48 4 54 10C60 16 60 26 54 32L32 54Z"
          stroke="currentColor"
          strokeWidth="2.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="none"
          className="animate-pulse"
        />
        {/* Pulse line */}
        <path
          d="M12 24H18L22 18L28 30L32 22L36 26H52"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="none"
          className="opacity-70"
        />
      </svg>
    </div>
  );
}

interface WelcomeViewProps {
  startButtonText: string;
  onStartCall: () => void;
}

export const WelcomeView = React.forwardRef<HTMLDivElement, WelcomeViewProps>(
  ({ startButtonText, onStartCall }, ref) => {
    return (
      <div
        ref={ref}
        className="relative flex min-h-screen items-center justify-center overflow-hidden"
      >
        {/* Animated background shapes */}
        <div className="bg-primary/10 absolute top-20 left-10 h-72 w-72 animate-pulse rounded-full blur-3xl" />
        <div
          className="bg-accent/10 absolute right-10 bottom-20 h-96 w-96 animate-pulse rounded-full blur-3xl"
          style={{ animationDelay: '1s' }}
        />

        <section className="relative z-10 flex max-w-2xl flex-col items-center justify-center px-4 text-center">
          <WelcomeImage />

          <h1 className="text-foreground from-primary to-accent animate-text-shimmer mb-3 bg-gradient-to-r bg-clip-text text-4xl font-bold text-transparent md:text-5xl">
            Wellness Companion
          </h1>

          <p className="text-foreground/90 mb-2 max-w-prose text-lg font-medium md:text-xl">
            Your Daily Check-In Partner
          </p>

          <p className="text-muted-foreground max-w-prose pt-2 text-sm leading-relaxed md:text-base">
            Take a mindful moment to reflect on your mood, energy, and intentions for the day.
            <br />
            <span className="text-primary font-medium">Let's make today count together.</span>
          </p>

          <Button
            variant="primary"
            size="lg"
            onClick={onStartCall}
            className="glow mt-8 w-72 transform rounded-xl py-6 text-lg font-semibold shadow-lg transition-all duration-300 hover:scale-105 hover:shadow-xl"
          >
            {startButtonText}
          </Button>

          {/* Feature highlights */}
          <div className="mt-12 grid w-full grid-cols-1 gap-6 md:grid-cols-3">
            <div className="glass rounded-xl p-4">
              <div className="mb-2 text-2xl">💬</div>
              <h3 className="text-foreground mb-1 font-semibold">Natural Voice</h3>
              <p className="text-muted-foreground text-xs">Powered by Murf Falcon TTS</p>
            </div>
            <div className="glass rounded-xl p-4">
              <div className="mb-2 text-2xl">🧠</div>
              <h3 className="text-foreground mb-1 font-semibold">Smart Insights</h3>
              <p className="text-muted-foreground text-xs">Track patterns over time</p>
            </div>
            <div className="glass rounded-xl p-4">
              <div className="mb-2 text-2xl">🔒</div>
              <h3 className="text-foreground mb-1 font-semibold">Private & Secure</h3>
              <p className="text-muted-foreground text-xs">Your data stays with you</p>
            </div>
          </div>
        </section>

        <div className="fixed bottom-5 left-0 z-20 flex w-full items-center justify-center">
          <p className="text-muted-foreground bg-background/50 max-w-prose rounded-full px-4 py-2 pt-1 text-xs leading-5 font-normal text-pretty backdrop-blur-sm md:text-sm">
            Built with ❤️ for the Murf AI Voice Agents Challenge | Powered by Murf Falcon
          </p>
        </div>
      </div>
    );
  }
);

WelcomeView.displayName = 'WelcomeView';
