from django.shortcuts import render

# ---------------------------------------------------------------------------
# Portfolio content. Edit here; templates render from these structures.
# ---------------------------------------------------------------------------

PROFILE = {
    "name": "Rahul Agarwal",
    "role": "AI Engineer",
    "tagline": "Generative AI · LLMs · Agentic AI · Computer Vision",
    "location": "Surat, Gujarat, India",
    "timezone": "IST (UTC+5:30), overlaps US mornings & EU afternoons",
    "email": "rekharahul.agarwal@gmail.com",
    "phone": "+91 88490 95957",
    "phone_raw": "+918849095957",
    "whatsapp": "https://wa.me/918849095957",
    "linkedin": "https://www.linkedin.com/in/rahul-agarwal-00044a191/",
    "resume": "myapp/assets/pdf/Rahul_Agarwal_AI_Engineer_Resume.pdf",
    "years": "2.7+",
}

STATS = [
    {"value": "2.7+", "label": "Years shipping AI to production"},
    {"value": "14+", "label": "AI & backend products delivered"},
    {"value": "3", "label": "Enterprise IIoT clients (BCCL, Mahindra, PCBL)"},
    {"value": "#1", "label": "IEEE MSP Cup 2022, R-10 Asia-Pacific"},
]

CLIENTS = [
    "BCCL (Coal India)", "Mahindra Logistics", "PCBL", "Texitle",
    "US HR Consultancy", "Aureate Labs", "Xconics", "Avinya Digital",
]

SERVICES = [
    {
        "icon": "agent",
        "title": "AI Agents & Agentic Workflows",
        "summary": "Multi-step agents that plan, call tools and finish real tasks instead of chatting about them.",
        "points": [
            "LangGraph state machines with tool calling & conditional routing",
            "ReAct / Chain-of-Thought planning, human-in-the-loop checkpoints",
            "MCP servers & tools that plug agents into your APIs and data",
            "Tracing, retries, cost caps and guardrails via LangSmith",
        ],
        "stack": ["LangGraph", "CrewAI", "AutoGen", "OpenAI Agents SDK", "MCP", "LangSmith"],
    },
    {
        "icon": "rag",
        "title": "RAG & Knowledge Assistants",
        "summary": "Chat with your docs, tickets and databases, with sources you can trust.",
        "points": [
            "Ingestion, chunking & embedding pipelines for PDFs, sites and DBs",
            "Hybrid retrieval on FAISS / PGVector, re-ranking, citations",
            "Graph-RAG & long-term memory with Neo4j + Graphiti",
            "Retrieval & answer-quality evals (Ragas, DeepEval) before anything ships",
        ],
        "stack": ["LlamaIndex", "Pinecone", "Qdrant", "PGVector", "Neo4j", "Ragas"],
    },
    {
        "icon": "llm",
        "title": "LLM Integration & GenAI Features",
        "summary": "Add GenAI to an existing product: content, summaries, extraction, copilots.",
        "points": [
            "OpenAI, Claude, Azure OpenAI, Gemini, Groq, Llama, Mistral, OpenRouter",
            "Structured outputs, prompt engineering & model routing for cost",
            "SEO/content generation pipelines that run at scale",
            "Fine-tuning (LoRA / QLoRA) and private models on Ollama / vLLM",
        ],
        "stack": ["OpenAI", "Claude", "Gemini", "Groq", "Ollama", "vLLM", "LoRA"],
    },
    {
        "icon": "voice",
        "title": "Voice AI & Automation",
        "summary": "Voice agents and outbound automation that save your team hours every week.",
        "points": [
            "LLM voice agents on Twilio, Vapi, Retell or LiveKit with Whisper / Deepgram + ElevenLabs",
            "Cold-email & campaign automation (Instantly, sequencing)",
            "LLM-powered scraping & data extraction across platforms",
            "n8n / Make / Zapier workflows and browser extensions",
        ],
        "stack": ["Whisper", "ElevenLabs", "Vapi", "Twilio", "n8n", "Playwright"],
    },
    {
        "icon": "vision",
        "title": "Computer Vision Systems",
        "summary": "Detection, recognition and tracking models wired into real-time alerting backends.",
        "points": [
            "Object detection (YOLO), face recognition & ANPR",
            "OCR (PaddleOCR, Tesseract), pose estimation, object tracking",
            "RTSP camera streams, edge AI on Jetson / TensorRT, MQTT to cloud",
            "Real-time alerts & dashboards for industrial sites",
        ],
        "stack": ["YOLOv8", "OpenCV", "DeepSORT", "TensorRT", "PaddleOCR", "MQTT"],
    },
    {
        "icon": "backend",
        "title": "AI Backends, APIs & Deployment",
        "summary": "The production layer around the model: APIs, queues, databases, cloud.",
        "points": [
            "FastAPI / Django / Node.js microservices & REST APIs",
            "PostgreSQL, MySQL, MongoDB schema & system design",
            "Docker and GitHub Actions; deploys on AWS, GCP and Azure, analytics on BigQuery",
            "Monitoring, logging and cost visibility from day one",
        ],
        "stack": ["FastAPI", "Celery", "Redis", "Docker", "AWS", "GCP", "BigQuery"],
    },
]

ENGAGEMENTS = [
    {
        "name": "AI Discovery Sprint",
        "duration": "1 week",
        "for": "You have an idea or a messy AI prototype.",
        "includes": [
            "Use-case & data audit",
            "Model / framework selection with cost estimate",
            "Architecture diagram + build roadmap",
            "Small working proof-of-concept",
        ],
    },
    {
        "name": "MVP Build",
        "duration": "3–6 weeks",
        "for": "You need an agent, RAG app or AI feature live with users.",
        "includes": [
            "End-to-end build: model, backend, API, basic UI",
            "Evals & tracing set up (LangSmith)",
            "Dockerised deploy to your cloud",
            "Handover docs + walkthrough call",
        ],
        "featured": True,
    },
    {
        "name": "Ongoing AI Engineer",
        "duration": "Monthly",
        "for": "You want a dedicated AI engineer on your team.",
        "includes": [
            "Fixed weekly hours, async + live standups",
            "New features, prompt & model iteration",
            "Monitoring, cost & quality tuning",
            "Priority support",
        ],
    },
]

PROCESS = [
    {"step": "01", "title": "Discover", "text": "Short call to map the business goal, data, constraints and what \"done\" means. You get a written scope."},
    {"step": "02", "title": "Prototype", "text": "A thin working slice in days, not weeks, so we can test with real inputs and pick the right models."},
    {"step": "03", "title": "Build & Evaluate", "text": "Production code with tests, evals and tracing. Weekly demos and a shared progress board."},
    {"step": "04", "title": "Ship & Support", "text": "Deploy to your cloud, hand over docs, then monitor quality and cost after launch."},
]

SKILL_GROUPS = [
    {"title": "GenAI & Agentic AI", "items": ["LangChain", "LangGraph", "LangSmith", "CrewAI", "AutoGen", "OpenAI Agents SDK", "LlamaIndex", "Pydantic AI", "AI Agents", "Multi-Agent Systems", "Tool / Function Calling", "MCP Tooling", "ReAct", "Chain-of-Thought", "Structured Outputs (JSON)", "Agent Memory", "Human-in-the-Loop"]},
    {"title": "RAG & Prompting", "items": ["RAG Pipelines", "Document Ingestion & Chunking", "Semantic Search", "Hybrid Search", "Graph RAG", "Prompt Engineering", "Context Engineering", "Prompt Templates & Few-Shot", "Hallucination Reduction"]},
    {"title": "LLM APIs & Models", "items": ["OpenAI", "Anthropic Claude", "Azure OpenAI", "Google Gemini", "Groq", "Hugging Face", "Llama", "Mistral", "OpenRouter", "Model Routing & Cost Optimisation", "Token & Latency Optimisation"]},
    {"title": "Fine-Tuning & Local LLMs", "items": ["LoRA / QLoRA", "PEFT", "Ollama", "vLLM", "LM Studio", "GGUF Quantisation", "HF Transformers"]},
    {"title": "LLM Evals & Safety", "items": ["LangSmith Tracing", "Langfuse", "Ragas", "DeepEval", "Guardrails AI", "Prompt-Injection Defence", "LLM-as-Judge Evals"]},
    {"title": "Voice AI", "items": ["Voice AI Agents", "Whisper", "Deepgram", "ElevenLabs", "Twilio", "Vapi", "Retell AI", "LiveKit", "Speech-to-Text", "Text-to-Speech", "Conversational AI"]},
    {"title": "Vector DBs & Storage", "items": ["FAISS", "PGVector", "Pinecone", "ChromaDB", "Qdrant", "Weaviate", "Milvus", "Elasticsearch", "Embeddings", "Neo4j", "Graphiti", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Supabase", "Firebase", "SQLAlchemy"]},
    {"title": "Document AI & OCR", "items": ["Tesseract", "PaddleOCR", "EasyOCR", "Docling", "Unstructured", "PyMuPDF", "PDF / Document Parsing"]},
    {"title": "Computer Vision", "items": ["Ultralytics YOLOv8 / v11", "OpenCV", "ANPR", "Face Recognition", "Pose Estimation", "MediaPipe", "DeepSORT / ByteTrack", "RTSP Streams", "Real-Time Video Analytics", "ONNX", "TensorRT", "NVIDIA Jetson / DeepStream", "Image Processing"]},
    {"title": "Data & ML", "items": ["PyTorch", "Scikit-learn", "Pandas", "NumPy", "NLP", "Deep Learning", "Data Preprocessing", "Model Inference & Deployment", "AI Image Generation", "Jupyter / Colab"]},
    {"title": "Backend & APIs", "items": ["Python", "FastAPI", "Pydantic", "Async Python", "Django", "Flask", "Node.js", "Express.js", "REST APIs", "GraphQL", "WebSockets", "Celery", "RabbitMQ", "Swagger / OpenAPI", "JWT Auth", "Microservices", "System Design", "Postman"]},
    {"title": "Frontend & Product", "items": ["TypeScript", "JavaScript", "React.js", "Next.js", "Tailwind CSS", "Streamlit", "Chrome Extensions", "SaaS Product Development", "Dashboards"]},
    {"title": "Cloud & DevOps", "items": ["AWS (EC2, S3)", "GCP", "BigQuery", "Azure", "Docker", "Docker Compose", "GitHub Actions", "CI/CD", "Nginx", "Prometheus / Grafana", "Linux", "Vercel", "Git & GitHub"]},
    {"title": "Automation & Scraping", "items": ["n8n", "Make", "Zapier", "Playwright", "Selenium", "Scrapy", "BeautifulSoup", "Crawl4AI", "Workflow Automation", "Cold Email Automation", "Instantly", "SEO Automation", "Ad Analytics"]},
    {"title": "IoT & Hardware", "items": ["MQTT", "IIoT", "IMU Sensors", "Signal Processing", "Edge AI"]},
    {"title": "Languages & Ways of Working", "items": ["Python", "JavaScript", "TypeScript", "C++", "SQL", "Agile / Scrum", "Client Communication", "Technical Documentation", "Requirement Analysis"]},
]

MARQUEE = [
    "LangGraph", "LangChain", "CrewAI", "LlamaIndex", "OpenAI", "Claude", "Gemini", "Azure OpenAI", "Groq",
    "Llama", "Mistral", "Ollama", "vLLM", "Hugging Face", "MCP", "Pinecone", "Qdrant", "FAISS", "PGVector",
    "Neo4j", "Whisper", "ElevenLabs", "n8n", "FastAPI", "PyTorch", "YOLO", "Docker", "AWS", "GCP", "BigQuery",
]

PROJECTS = [
    {
        "slug": "ad-analytics",
        "title": "AI Ad & E-commerce Analytics Platform",
        "client": "Aureate Labs · SaaS",
        "category": "genai",
        "category_label": "GenAI SaaS",
        "featured": True,
        "summary": "One dashboard that unifies ad-platform and store data, with an LLM layer that explains performance and suggests what to do next.",
        "problem": "Marketers jump between ad managers and store analytics, then guess what to change.",
        "solution": "Unified data model + LLM insights, AI ad-creative generation, campaign planning and automated optimisation suggestions.",
        "impact": ["Ad + commerce data in one view", "LLM insights in plain English", "AI-generated ad creatives"],
        "stack": ["LLMs", "Node.js", "TypeScript", "React", "GCP"],
    },
    {
        "slug": "seo-platforms",
        "title": "AI SEO & Content Generation Platforms",
        "client": "Aureate Labs · 2 SaaS products",
        "category": "genai",
        "category_label": "GenAI SaaS",
        "featured": False,
        "summary": "Two SaaS products in the space of Ahrefs, Semrush, SurferSEO and Outrank: keyword research, content analysis and LLM article pipelines.",
        "problem": "Teams need ranking-ready content at volume without hiring a writing department.",
        "solution": "Keyword & SERP analysis tools feeding multi-step LLM pipelines that outline, draft and optimise articles at scale.",
        "impact": ["SEO-optimised articles at scale", "Keyword research & content scoring", "Two products, one shared AI core"],
        "stack": ["LLM Pipelines", "Prompt Engineering", "Node.js", "TypeScript", "GCP"],
    },
    {
        "slug": "voice-agent",
        "title": "AI Voice Agent for HR",
        "client": "HR Consultancy · USA",
        "category": "agents",
        "category_label": "Agentic AI",
        "featured": True,
        "summary": "Recruiting dashboard where an AI voice agent screens candidates by phone: upload a list, schedule a campaign and track every call through the pipeline.",
        "problem": "Recruiters spent hours on repetitive screening and follow-up calls.",
        "solution": "LLM voice agent for inbound and outbound calls, CSV/Excel candidate import, n8n-scheduled campaigns, video interviews and call logs with W2 / relocation / availability evaluation.",
        "impact": ["Inbound + outbound AI screening calls", "Candidate pipeline with auto evaluation", "Campaign scheduling via n8n"],
        "stack": ["Python", "LLM APIs", "Voice AI", "n8n", "React"],
        "url": "https://ai-voice-agent-liart.vercel.app/",
    },
    {
        "slug": "maabaap",
        "title": "MaaBaap: Little Reminders from Home",
        "client": "Personal product",
        "category": "product",
        "category_label": "Desktop App",
        "featured": True,
        "summary": "Desktop app that drops caring reminders at the top of your screen (eat, drink water, stretch, call home) in a familiar Maa or Papa voice.",
        "problem": "Busy days at a desk make people skip meals, water, breaks and calls home.",
        "solution": "Cross-platform desktop app with scheduled sticker reminders, family voices in 10 languages and 5 moods, quiet hours, and settings that stay on the device.",
        "impact": ["10 languages, 5 voice moods", "Mac, Windows & Linux builds", "Free + one-time Pro (₹199)"],
        "stack": ["Desktop App", "Voice", "10 Languages", "Local-first", "Vercel"],
        "url": "https://gharwale-ten.vercel.app/",
    },
    {
        "slug": "voice-dashboard",
        "title": "VoiceAI: AI Voice Assistant Dashboard",
        "client": "Personal product",
        "category": "agents",
        "category_label": "Voice AI",
        "featured": False,
        "summary": "Web dashboard for an AI voice assistant: sign in, manage the assistant's voice calls and review every conversation in one place.",
        "problem": "Voice-assistant calls are hard to track and review without a central place to manage them.",
        "solution": "Authenticated dashboard for managing AI voice calls, with call history and conversation review.",
        "impact": ["AI voice call management", "Secure sign-in & accounts", "Live on Vercel"],
        "stack": ["Voice AI", "LLM APIs", "React", "Vercel"],
        "url": "https://voice-ai-dashboard-umber.vercel.app/",
    },
    {
        "slug": "coal-mine",
        "title": "Coal-Mine Driver Safety & Vehicle ID",
        "client": "BCCL (Coal India) · via Xconics",
        "category": "vision",
        "category_label": "Computer Vision",
        "featured": False,
        "summary": "Face recognition and ANPR at mine gates: verifies drivers, flags unsafe driving and logs every truck automatically.",
        "problem": "Manual gate logs and no reliable check on who is driving heavy vehicles.",
        "solution": "FastAPI backend running face recognition, unsafe-driving detection and number-plate recognition, logged via REST APIs.",
        "impact": ["Automatic truck entry logs", "Driver identity verification", "Unsafe-driving alerts"],
        "stack": ["FastAPI", "Face Recognition", "ANPR", "PostgreSQL", "AWS S3"],
    },
    {
        "slug": "ai-studio",
        "title": "Modelly: AI Catalog Studio",
        "client": "Texitle",
        "category": "genai",
        "category_label": "GenAI",
        "featured": True,
        "summary": "AI catalog studio that turns plain garment photos into on-model photoshoots and flat-lay visuals using generative image models.",
        "problem": "Product photoshoots are slow and expensive for every new SKU.",
        "solution": "Generative image pipelines exposed through REST APIs for the client's frontend.",
        "impact": ["Photoshoot visuals without a shoot", "Flat-lay generation", "API-first for any frontend"],
        "stack": ["Python", "Generative AI", "Image Generation", "REST APIs"],
        "url": "https://ai-studio-lime-three.vercel.app/",
    },
    {
        "slug": "web-scraper",
        "title": "LLM-Powered AI Web Scraper",
        "client": "Avinya Digital Innovations",
        "category": "automation",
        "category_label": "Automation",
        "featured": False,
        "summary": "Describe the data you want in plain English; the LLM finds and structures it from the page.",
        "problem": "Writing and maintaining a scraper per site does not scale.",
        "solution": "Crawler + Groq-hosted LLM extraction with a Streamlit UI and multiple export formats.",
        "impact": ["10+ platforms supported", "~10 s per page", "CSV / JSON / Excel export"],
        "stack": ["Python", "Groq", "Crawl4AI", "Streamlit"],
    },
    {
        "slug": "upwork-extension",
        "title": "Upwork Job Alerts & AI Cover Letters",
        "client": "Avinya Digital Innovations",
        "category": "automation",
        "category_label": "Automation",
        "featured": False,
        "summary": "Browser extension + web app for instant job alerts and personalised AI-written proposals.",
        "problem": "The first good proposals win, and writing them by hand is slow.",
        "solution": "Real-time alerts plus GenAI cover letters tailored to the freelancer's profile, with media auto-attached.",
        "impact": ["Apply in under 2 minutes", "Personalised GenAI proposals", "Extension + website"],
        "stack": ["JavaScript", "Python", "LLM APIs"],
    },
    {
        "slug": "cold-email",
        "title": "Cold Email Automation System",
        "client": "Aureate Labs",
        "category": "automation",
        "category_label": "Automation",
        "featured": False,
        "summary": "Outbound engine that sets up campaigns, sequences and follow-ups with AI-personalised copy.",
        "problem": "Outbound setup and follow-ups ate hours of manual work each week.",
        "solution": "Automated workflows on Instantly and integrated tools for setup, sequencing and follow-ups.",
        "impact": ["Campaign setup automated", "AI-personalised sequences", "Hands-off follow-ups"],
        "stack": ["Instantly", "Node.js", "LLM APIs"],
    },
    {
        "slug": "anti-theft",
        "title": "Anti-Theft Surveillance System",
        "client": "PCBL · via Xconics",
        "category": "vision",
        "category_label": "Computer Vision",
        "featured": False,
        "summary": "Real-time object detection on plant cameras that raises alerts the moment something looks wrong.",
        "problem": "Security teams cannot watch every camera feed all the time.",
        "solution": "Object-detection models behind FastAPI with event images stored and served from AWS S3.",
        "impact": ["Real-time alerts", "Evidence images on S3", "Plugs into existing CCTV"],
        "stack": ["FastAPI", "YOLO", "OpenCV", "AWS S3"],
    },
    {
        "slug": "forklift",
        "title": "Forklift Monitoring (IIoT)",
        "client": "Mahindra Logistics · via Xconics",
        "category": "iot",
        "category_label": "Industrial IoT",
        "featured": False,
        "summary": "Live tracking of forklift engine status, load activity and zone movement across the warehouse.",
        "problem": "No visibility into how forklifts were actually being used.",
        "solution": "FastAPI backend consuming MQTT telemetry into PostgreSQL for productivity dashboards.",
        "impact": ["Engine & load status live", "Zone movement tracking", "Productivity reporting"],
        "stack": ["FastAPI", "MQTT", "PostgreSQL"],
    },
    {
        "slug": "hand-movement",
        "title": "Hand Movement Detection",
        "client": "Industrial harvesting · via Xconics",
        "category": "iot",
        "category_label": "Industrial IoT",
        "featured": False,
        "summary": "IMU-sensor motion analysis that finds the most efficient plucking movements for workers.",
        "problem": "Wasted hand movements lowered harvesting output.",
        "solution": "Motion-tracking from IMU sensors to classify gestures and surface efficiency insights.",
        "impact": ["Less wasted movement", "Gesture classification", "Efficiency insights"],
        "stack": ["Python", "IMU Sensors", "Signal Processing"],
    },
    {
        "slug": "pose",
        "title": "Exercise Pose Recognition & Rep Counter",
        "client": "IEEE MSP Cup 2022 · 1st place",
        "category": "vision",
        "category_label": "Computer Vision",
        "featured": False,
        "summary": "Pose-estimation trainer that counts reps, times sets and corrects form in real time.",
        "problem": "People train alone with no feedback on form.",
        "solution": "MediaPipe pose landmarks + joint-angle logic for rep counting, guidance and error detection.",
        "impact": ["1st place, R-10 Asia-Pacific", "Real-time form feedback", "Rep counter & timer"],
        "stack": ["Python", "MediaPipe", "OpenCV"],
    },
]

# Images used by the home page project cards (old design slots).
PROJECT_IMAGES = {
    "voice-agent": "projects/voice-agent.jpg",
    "ai-studio": "projects/ai-studio.jpg",
    "voice-dashboard": "projects/voice-dashboard.jpg",
    "maabaap": "projects/maabaap.jpg",
}
for _p in PROJECTS:
    # Real screenshot when we have one; otherwise the template draws a branded cover.
    _p["image"] = "myapp/assets/images/" + PROJECT_IMAGES[_p["slug"]] if _p["slug"] in PROJECT_IMAGES else None

# Home page "My Expertise" circles.
EXPERTISE = [
    {"label": "Generative AI & LLMs", "value": 95, "icon": "https://img.icons8.com/color/48/artificial-intelligence.png"},
    {"label": "AI Agents (LangGraph, CrewAI)", "value": 92, "icon": "https://img.icons8.com/color/48/robot-2.png"},
    {"label": "RAG & Vector Databases", "value": 92, "icon": "https://img.icons8.com/color/48/database.png"},
    {"label": "Python & FastAPI", "value": 95, "icon": "https://img.icons8.com/?size=48&id=13441&format=png"},
    {"label": "Computer Vision", "value": 92, "icon": "https://img.icons8.com/?size=48&id=apebs8fnmi4m&format=png"},
    {"label": "Voice AI Agents", "value": 88, "icon": "https://img.icons8.com/color/48/microphone.png"},
    {"label": "Machine Learning & PyTorch", "value": 88, "icon": "https://img.icons8.com/?size=48&id=fTkqveCX0blI&format=png"},
    {"label": "Automation & Scraping", "value": 93, "icon": "https://img.icons8.com/color/48/web-scraper.png"},
]

PROJECT_TABS = [
    {"id": "tab2", "label": "GenAI & Agents", "cats": ["genai", "agents"]},
    {"id": "tab3", "label": "Computer Vision", "cats": ["vision"]},
    {"id": "tab4", "label": "Automation", "cats": ["automation"]},
    {"id": "tab5", "label": "Industrial IoT", "cats": ["iot"]},
    {"id": "tab6", "label": "Products", "cats": ["product"]},
]
for _t in PROJECT_TABS:
    _t["projects"] = [p for p in PROJECTS if p["category"] in _t["cats"]]

TICKER = ["AI Agents", "Generative AI", "RAG Systems", "LLM Apps", "Voice AI", "Computer Vision", "Automation", "Multi-Agent Systems"]

PROJECT_FILTERS = [
    ("all", "All work"),
    ("agents", "Agentic AI"),
    ("genai", "GenAI"),
    ("vision", "Computer Vision"),
    ("automation", "Automation"),
    ("iot", "Industrial IoT"),
    ("product", "Products"),
]

EXPERIENCE = [
    {
        "company": "Aureate Labs",
        "role": "AI Specialist",
        "period": "Feb 2026 – Present",
        "place": "Surat, Gujarat · On-site",
        "points": [
            "Building AI-powered SaaS products for SEO, AI content generation, marketing automation and ad analytics using LLMs.",
            "Shipping Generative AI features, cold-email and campaign automation with Node.js, TypeScript, React and GCP.",
        ],
    },
    {
        "company": "Xconics",
        "role": "Python & AI/ML Engineer",
        "period": "Apr 2025 – Feb 2026",
        "place": "Mumbai, Maharashtra",
        "points": [
            "Built FastAPI backends for Computer Vision and Industrial IoT systems for BCCL, Mahindra Logistics and PCBL.",
            "Deployed object detection, face recognition and ANPR models with MQTT, PostgreSQL and AWS S3 for real-time alerts.",
        ],
    },
    {
        "company": "Avinya Digital Innovations",
        "role": "Python Developer & AI/ML Engineer",
        "period": "Jan 2024 – Mar 2025",
        "place": "Surat, Gujarat",
        "points": [
            "Developed Python backends and automation tools integrating Generative AI, LLMs and computer vision.",
            "Built LLM-powered web scraping and job-automation products used across 10+ platforms.",
            "Recognised with a SAFAL Certificate of Appreciation for client delivery.",
        ],
    },
    {
        "company": "eInfochips (An Arrow Company)",
        "role": "Summer Intern, ASIC Flow Orientation",
        "period": "Jul 2023 – Aug 2023",
        "place": "Ahmedabad, Gujarat",
        "points": [],
    },
]

ACHIEVEMENTS = [
    {"title": "1st Place, IEEE Multimedia Signal Processing Cup 2022", "meta": "R-10 Asia-Pacific level · IEEE SPS Gujarat Section · Aug 2022"},
    {"title": "SSIP Grant of ₹1 Lakh, SKYBOUND Drone Delivery", "meta": "Startup Support & Innovation Program, Govt. of Gujarat · 2024"},
    {"title": "SAFAL Certificate of Appreciation", "meta": "Recognised for client delivery at Avinya"},
    {"title": "100 Days of Code: Python Pro Bootcamp", "meta": "Udemy, Dr. Angela Yu · 52 hours"},
]

FAQS = [
    {"q": "Which LLM should my product use?", "a": "It depends on quality, latency, cost and data-privacy needs. I usually prototype on 2–3 providers (e.g. OpenAI, Gemini, Llama via Groq) against your real inputs and pick based on measured results, often routing simple calls to a cheaper model."},
    {"q": "Can you work with our existing codebase and cloud?", "a": "Yes. Most of my work plugs AI into existing Python, Node.js or Django systems on AWS, GCP or Azure. I adapt to your repo conventions, CI/CD and review process."},
    {"q": "How do you keep AI output reliable?", "a": "Structured outputs, retrieval with citations, eval sets built from your real data, LangSmith tracing, and guardrails and fallbacks for when a model gets it wrong."},
    {"q": "What about data privacy?", "a": "Your data stays in your accounts. I can use Azure OpenAI or self-hosted open models (Llama, Mistral) when data cannot leave your environment, and I sign NDAs."},
    {"q": "What time zone do you work in?", "a": "IST (UTC+5:30). I overlap with US mornings and EU afternoons and reply within a few hours on working days."},
]

INSIGHTS = [
    "https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7310661228241018880?collapsed=1",
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7257285209019047936?collapsed=1",
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7256989285885562881?collapsed=1",
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7256536617450913792?collapsed=1",
    "https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7204868244208308224?collapsed=1",
    "https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7201665127601876992?collapsed=1",
]


def _ctx(page, **extra):
    ctx = {"profile": PROFILE, "page": page}
    ctx.update(extra)
    return ctx


def index_view(request):
    return render(request, "index.html", _ctx(
        "home",
        stats=STATS,
        clients=CLIENTS,
        services=SERVICES,
        featured=sorted([p for p in PROJECTS if p["featured"]], key=lambda p: "url" not in p),
        projects=PROJECTS,
        project_tabs=PROJECT_TABS,
        expertise=EXPERTISE,
        ticker=TICKER,
        insights=INSIGHTS,
        process=PROCESS,
        marquee=MARQUEE,
        achievements=ACHIEVEMENTS[:2],
    ))


def about_view(request):
    return render(request, "about.html", _ctx(
        "about",
        ticker=TICKER,
        clients=CLIENTS,
        experience=EXPERIENCE,
        skill_groups=SKILL_GROUPS,
        achievements=ACHIEVEMENTS,
        stats=STATS,
    ))


def services_view(request):
    return render(request, "services.html", _ctx(
        "services",
        services=SERVICES,
        engagements=ENGAGEMENTS,
        process=PROCESS,
        faqs=FAQS,
    ))


def portfolio_view(request):
    return render(request, "portfolio.html", _ctx(
        "portfolio",
        projects=PROJECTS,
        filters=PROJECT_FILTERS,
    ))


def blog_view(request):
    return render(request, "blog.html", _ctx("insights", insights=INSIGHTS, clients=CLIENTS))


def contact_view(request):
    return render(request, "contact.html", _ctx("contact", services=SERVICES))
