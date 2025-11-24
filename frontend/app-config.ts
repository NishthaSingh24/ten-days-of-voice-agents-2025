export interface AppConfig {
  pageTitle: string;
  pageDescription: string;
  companyName: string;

  supportsChatInput: boolean;
  supportsVideoInput: boolean;
  supportsScreenShare: boolean;
  isPreConnectBufferEnabled: boolean;

  logo: string;
  startButtonText: string;
  accent?: string;
  logoDark?: string;
  accentDark?: string;

  // for LiveKit Cloud Sandbox
  sandboxId?: string;
  agentName?: string;
}

export const APP_CONFIG_DEFAULTS: AppConfig = {
  companyName: 'Wellness Companion',
  pageTitle: 'Wellness Companion - Daily Check-In',
  pageDescription: 'Your supportive daily wellness check-in companion powered by Murf Falcon',

  supportsChatInput: true,
  supportsVideoInput: false,
  supportsScreenShare: false,
  isPreConnectBufferEnabled: true,

  logo: '/lk-logo.svg',
  accent: '#2563eb', // Vibrant blue
  logoDark: '/lk-logo-dark.svg',
  accentDark: '#3b82f6', // Lighter blue for dark mode
  startButtonText: 'Start Check-In ✨',

  // for LiveKit Cloud Sandbox
  sandboxId: undefined,
  agentName: undefined,
};
