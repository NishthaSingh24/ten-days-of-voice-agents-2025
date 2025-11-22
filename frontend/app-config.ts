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
  companyName: 'Brew Haven Café',
  pageTitle: 'Brew Haven Café - AI Barista',
  pageDescription: 'Order your favorite coffee with our AI barista powered by Murf Falcon',

  supportsChatInput: true,
  supportsVideoInput: false,
  supportsScreenShare: false,
  isPreConnectBufferEnabled: true,

  logo: '/lk-logo.svg',
  accent: '#8B4513', // Coffee brown
  logoDark: '/lk-logo-dark.svg',
  accentDark: '#D2691E', // Chocolate
  startButtonText: 'Start Ordering ☕',

  // for LiveKit Cloud Sandbox
  sandboxId: undefined,
  agentName: undefined,
};
