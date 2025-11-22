# 🚀 Quick Start Guide - Day 2 Coffee Shop Barista

## ✅ Prerequisites Check

Make sure you have:

- ✅ Python 3.9+ installed
- ✅ Node.js 18+ installed
- ✅ pnpm installed (`npm install -g pnpm`)
- ✅ uv installed (`pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- ✅ LiveKit server installed

## 📝 Environment Setup

### 1. Backend Environment (.env.local)

Create or verify `backend/.env.local` with:

```env
# LiveKit Server
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret

# Murf Falcon TTS
MURF_API_KEY=your_murf_api_key_here

# Google Gemini LLM
GOOGLE_API_KEY=your_google_api_key_here

# Deepgram STT
DEEPGRAM_API_KEY=your_deepgram_api_key_here
```

### 2. Frontend Environment (.env.local)

Create or verify `frontend/.env.local` with:

```env
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
```

## 🎬 Start the Application

### Option 1: All-in-One (Recommended)

Open **3 separate terminals** in the project root:

#### Terminal 1: LiveKit Server

```bash
livekit-server --dev
```

Wait for: `starting  {"addr": ":7880", "nodeID": "..."}`

#### Terminal 2: Backend Agent

```bash
cd backend
uv sync
uv run python src/agent.py dev
```

Wait for: `Agent started`

#### Terminal 3: Frontend

```bash
cd frontend
pnpm install
pnpm dev
```

Wait for: `Local: http://localhost:3000`

### Option 2: Using Bash Script (Linux/Mac)

```bash
chmod +x start_app.sh
./start_app.sh
```

## 🎤 Test the Agent

1. Open browser: **http://localhost:3000**
2. Click **"Start Ordering ☕"**
3. Allow microphone access
4. Start talking!

### Test Conversation Script

Try this conversation to test all features:

```
You: "Hi there!"
→ Wait for greeting from Bella

You: "What coffee drinks do you have?"
→ Agent shows menu

You: "I'll have a large latte with oat milk"
→ Agent adds to order

You: "Also add a chocolate muffin"
→ Agent adds muffin

You: "That's all"
→ Agent asks for name

You: "Sarah" (or your name)
→ Agent reviews order

You: "Yes, that's correct"
→ Agent finalizes order
```

## 🎥 Recording Your Demo

### Setup

1. **Screen Recording Tool**: OBS Studio, QuickTime, or Windows Game Bar
2. **Audio**: Make sure microphone is captured
3. **Resolution**: 1080p recommended
4. **Length**: 60-90 seconds

### Recording Steps

1. **Start Recording**
2. **Show Welcome Screen** (5 seconds)
   - "This is Brew Haven Café, powered by Murf Falcon"
3. **Click "Start Ordering"** (2 seconds)
4. **Have a Natural Conversation** (40-60 seconds)
   - Order a drink with customizations
   - Add a pastry
   - Give your name
   - Confirm order
5. **Show Final Order Summary** (5-10 seconds)
6. **Stop Recording**

### Editing Tips

- Trim any dead space at start/end
- Add captions highlighting key moments:
  - "Menu Display"
  - "Adding Customizations"
  - "Order Summary"
  - "Powered by Murf Falcon"

## 📱 LinkedIn Posting

### Post Template

```
🚀 Day 2 Complete! Coffee Shop Barista Voice Agent ☕

Just built an AI barista that takes coffee orders completely by voice!

✨ Features:
• Interactive menu browsing (coffee, tea, pastries)
• Smart order customization (sizes, milk alternatives, syrups)
• Real-time price calculation
• Natural conversation flow
• Order confirmation with name

🔥 Tech Stack:
• Murf Falcon - The fastest TTS API
• LiveKit Agents Framework
• Google Gemini 2.5 Flash
• Deepgram Nova-3

The agent uses function tools to:
✅ Display menu categories
✅ Add items with customizations
✅ Track order state
✅ Calculate pricing
✅ Finalize orders

Just like ordering from a real barista, but powered by AI!

#MurfAIVoiceAgentsChallenge #10DaysofAIVoiceAgents #VoiceAI
#LiveKit #MurfFalcon #AI #CoffeeShop #TechChallenge

@Murf AI @Starbucks @Cafe Coffee Day @Blue Tokai Coffee

[Attach your video here]
```

### Posting Checklist

- [ ] Video is under 5 minutes
- [ ] Mentioned "Murf Falcon - fastest TTS API"
- [ ] Used hashtags: #MurfAIVoiceAgentsChallenge #10DaysofAIVoiceAgents
- [ ] Tagged Murf AI
- [ ] Tagged a coffee brand (optional but recommended)
- [ ] Posted before 9 PM IST

## 📤 Submit Your Work

After posting on LinkedIn:

1. Go to: https://forms.gle/ge58Ne66wfPN98Pg7
2. Fill in:
   - Your name
   - LinkedIn post URL
   - GitHub repo URL (if you pushed to GitHub)
   - Any additional notes

## 🐛 Troubleshooting

### Backend won't start

```bash
cd backend
uv sync --force
uv run python src/agent.py download-files
```

### Frontend won't start

```bash
cd frontend
rm -rf node_modules pnpm-lock.yaml
pnpm install
```

### LiveKit connection fails

- Check LiveKit server is running: `ps aux | grep livekit-server`
- Verify port 7880 is not in use
- Check `.env.local` credentials match in both frontend and backend

### Agent doesn't respond

- Check microphone permissions in browser
- Verify all API keys in `.env.local`
- Check backend terminal for errors
- Refresh browser page

### No audio from agent

- Check system volume
- Verify Murf API key is valid
- Check browser audio permissions

## 💡 Tips for a Great Demo

1. **Speak clearly** - Treat it like ordering at a real coffee shop
2. **Test first** - Do a practice run before recording
3. **Show variety** - Order different items, add customizations
4. **Highlight features** - Mention "Powered by Murf Falcon" in your video
5. **Be enthusiastic** - Show excitement about what you built!

## 🎯 Success Criteria

Your Day 2 is complete when:

- ✅ Agent takes coffee orders via voice
- ✅ Menu display works
- ✅ Order customization works (size, extras)
- ✅ Price calculation is accurate
- ✅ Order summary shows correctly
- ✅ Video recorded and posted on LinkedIn
- ✅ Form submitted before deadline

---

**Good luck with Day 2! ☕🚀**

Need help? Check the [DAY2_README.md](DAY2_README.md) for detailed documentation.
