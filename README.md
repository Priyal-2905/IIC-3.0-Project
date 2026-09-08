<div align="center">

```
████████╗ █████╗ ████████╗    ███████╗ █████╗ ██╗  ██╗ █████╗ ██╗   ██╗██╗  ██╗
╚══██╔══╝██╔══██╗╚══██╔══╝    ██╔════╝██╔══██╗██║  ██║██╔══██╗╚██╗ ██╔╝██║ ██╔╝
   ██║   ███████║   ██║       ███████╗███████║███████║███████║ ╚████╔╝ █████╔╝ 
   ██║   ██╔══██║   ██║       ╚════██║██╔══██║██╔══██║██╔══██║  ╚██╔╝  ██╔═██╗ 
   ██║   ██║  ██║   ██║       ███████║██║  ██║██║  ██║██║  ██║   ██║   ██║  ██╗
   ╚═╝   ╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
```

### **Tat Sahayak** — *Proactive Habitation Intelligence*
**Intelligent Identification of Hazard-Based Red Zones, Carrying Capacity Assessment & Immediate Relocation Needs**

[![Live Platform](https://img.shields.io/badge/_Live_Platform-www.tatsahayk.in-0ea5e9?style=for-the-badge)](http://www.tatsahayk.in)
[![Docker](https://img.shields.io/badge/Deployed_with-Docker-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/Frontend-React_+_Vite-61DAFB?style=for-the-badge&logo=react)](https://react.dev)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL_+_PostGIS-4169E1?style=for-the-badge&logo=postgresql)](https://postgresql.org)
[![PyTorch](https://img.shields.io/badge/ML_Engine-PyTorch-EE4C2C?style=for-the-badge&logo=pytorch)](https://pytorch.org/)

> *"From reactive disaster response to predictive habitation security."*

</div>

---

## The Challenge

Rapid urbanization, climate change, and geographic instability have pushed human habitations into highly vulnerable ecological zones. Governments and disaster management authorities lack the dynamic, real-time spatial intelligence required to proactively identify high-risk areas before catastrophes occur.

| Crisis Point | Ground Reality |
|---|---|
| Reactive Relocation | Evacuations currently happen *during* disasters, causing massive loss of life and resources. |
| Invisible Red Zones | Outdated geographic surveys fail to account for emerging micro-climatic and topographical shifts. |
| Overburdened Land | Authorities have no quantitative model for a region's **carrying capacity** (population vs. geological stability). |
| Disjointed Data | Satellite imagery, ground reports, and demographic data live in isolated silos, delaying critical decisions. |

**The core problem is a lack of predictive geospatial intelligence to move vulnerable populations *before* the ground gives way.**

---

## Solution: Tat Sahayak

**Tat Sahayak** is an AI-driven, microservices-based platform designed to shift disaster management from reactive to preventive. By fusing geospatial data, computer vision, and machine learning, the system calculates the structural limits of habitations, dynamically maps hazard-based red zones, and triages vulnerable populations for immediate relocation.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Data Ingestion (Satellite Imagery + Ground Surveys + Topo)     │
│        ↓                                                        │
│  API Gateway (FastAPI) routes to Local ML Microservice          │
│        ↓                                                        │
│  AI Engine Fires 3 Spatial Assessments in Parallel:             │
│        ↓                         ↓                         ↓    │
│   Red Zone Mapping      Carrying Capacity        Relocation     │
│   (Geological Risk)     (Pop. vs Stability)      Triage Matrix  │
│        ↓                                                        │
│  PostgreSQL/PostGIS performs spatial indexing and aggregation   │
│        ↓                                                        │
│  Verdict & Interactive Heatmaps Sent to Government Dashboard    │
│        ↓                                                        │
│  Actionable Evacuation/Relocation Orders Generated              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## System Architecture

Tat Sahayak is built on a modular, localized architecture ensuring complete data sovereignty and high-performance spatial processing without reliance on external cloud dependencies.

```
┌──────────────────────────────────────────────────────────────────────┐
│  LAYER 1 — CLIENT (WEB & MOBILE)                                     │
│  React + Vite · Multi-language UI · Mapbox/Leaflet Integration       │
│  Interactive Red Zone Heatmaps · Demographic input forms             │
└────────────────────────┬─────────────────────────────────────────────┘
                         │ REST / JWT Auth
┌────────────────────────▼─────────────────────────────────────────────┐
│  LAYER 2 — CORE API (BACKEND)                                        │
│  FastAPI · Asynchronous task routing · RBAC (Surveyor / Admin)       │
│  Orchestrates data flow between UI, Database, and ML services        │
└────────────────────────┬─────────────────────────────────────────────┘
                         │ gRPC / Internal HTTP
┌────────────────────────▼─────────────────────────────────────────────┐
│  LAYER 3 — LOCAL ML INFERENCE SERVICE                                │
│  PyTorch / FastAPI wrapper · Geospatial Vision Models (YOLO/ResNet)  │
│  NLP for survey analysis · Statistical Carrying Capacity Algorithms  │
└────────────────────────┬─────────────────────────────────────────────┘
                         │ Spatial Reads/Writes
┌────────────────────────▼─────────────────────────────────────────────┐
│  LAYER 4 — DATA & STORAGE                                            │
│  PostgreSQL + PostGIS (Spatial queries, geometries, bounding boxes)  │
│  MinIO (S3-compatible local object storage for imagery/drone data)   │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Core Intelligence Modules

### 1. Intelligent Red Zone Identification
Maps out highly vulnerable geographic sectors using multimodal data analysis.

*   **Geospatial Vision:** Local PyTorch vision models analyze satellite and drone imagery to detect soil erosion patterns, landslide scars, and flood plain encroachment.
*   **Topographical Scoring:** Evaluates slope gradients, soil composition data, and proximity to volatile water bodies.
*   **Dynamic Tagging:** Automatically generates bounding boxes via PostGIS, marking areas as `Safe`, `Warning`, or `Critical Red Zone`.

### 2. Carrying Capacity Assessment
Calculates the maximum demographic load a specific geographic zone can sustain.

*   **Algorithmic Evaluation:** Cross-references current population density against geological stability, water table limits, and infrastructure durability.
*   **Load Deficit Detection:** Identifies zones where the current population exceeds the safe carrying capacity by calculating the *Sustain Ratio*.
*   **Predictive Modeling:** Simulates seasonal stress (e.g., monsoons) to adjust capacity thresholds dynamically.

### 3. Immediate Relocation Triage
Translates analytical data into actionable human logistics.

*   **Vulnerability Indexing:** Assigns a risk score (0.0 to 100.0) to individual habitations based on Red Zone proximity and Capacity Deficit.
*   **Triage Matrix:** Automatically flags the top 10% most vulnerable settlements for immediate, priority relocation.
*   **Safe Zone Routing:** Identifies nearby "Green Zones" with surplus carrying capacity and calculates optimal relocation logistics.

---

## Government Control Center

Real-time command dashboard with complete jurisdictional and spatial control:

### Geospatial Dashboard
*   **Live Heatmaps:** Interactive map overlays visualizing Red Zones, population densities, and structural hazards.
*   **Micro-Level Filtering:** Drill down from state-level carrying capacity to specific village block vulnerabilities.
*   **Temporal Comparisons:** View sliding-window comparisons of ecological degradation over months or years.

### Relocation Management
*   **Triage Action Center:** One-click generation of relocation manifests for critically endangered habitations.
*   **Asset Allocation:** Connects identified risk zones with available disaster management assets (NDRF, SDRF transport).
*   **Progress Tracking:** Tracks the status of ongoing relocations and updates the carrying capacity of both the source (Red Zone) and destination (Green Zone) in real-time.

---

## Local Deployment & Infrastructure

The entire platform is containerized via Docker for rapid deployment on on-premise servers, ensuring sensitive demographic and geographic data remains secure.

*   **PostGIS for Spatial Logic:** Replaces standard geographic queries with advanced computations (e.g., `ST_Intersects`, `ST_Within`) natively in the database.
*   **MinIO Object Storage:** Self-hosted alternative for storing heavy satellite TIFF files and drone footage, fully compatible with S3 APIs.
*   **GPU-Accelerated Inference:** The ML microservice is configured to utilize local NVIDIA GPUs (CUDA) for rapid processing of high-resolution imagery.

---

## Tech Stack

```text
Frontend      React + Vite · Tailwind CSS · React-Leaflet (Mapping)
Core API      FastAPI (Python) · SQLAlchemy · Pydantic · JWT
ML Engine     PyTorch · OpenCV · HuggingFace Transformers · Scikit-learn
Database      PostgreSQL · PostGIS Extension (Spatial Analytics)
Storage       MinIO (Local S3-compatible Object Storage)
Deployment    Docker · Docker Compose · Nginx (Reverse Proxy)
Security      HTTPS/TLS · RBAC · Argon2 Hashing
```

---

## Getting Started

### Prerequisites
*   Docker & Docker Compose
*   NVIDIA GPU with CUDA toolkit (Optional, highly recommended for ML service)
*   Node.js 18+ (For local UI development)
*   Python 3.10+ (For local API/ML development)

### Quick Start (Docker Orchestration)

The easiest way to run Tat Sahayak is via the provided `docker-compose.yml`, which spins up the database, object storage, API, ML service, and frontend.

```bash
# Clone the repository
git clone https://github.com/your-org/tat-sahayak.git
cd tat-sahayak

# Configure environment variables
cp .env.example .env
# Edit .env to set database passwords, JWT secrets, and MinIO keys

# Build and start all microservices
docker-compose up --build -d
```

### Accessing the Services
*   **Frontend UI:** `http://localhost:3000`
*   **Core Backend API:** `http://localhost:8000/docs`
*   **ML Inference Service:** `http://localhost:8001/docs`
*   **MinIO Console:** `http://localhost:9001`

---

## Development Setup

If you prefer to run the services individually for development:

### 1. Database & Storage
```bash
# Start only the infrastructure containers
docker-compose up -d db minio
```

### 2. ML Inference Service
```bash
cd ml_service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Download required local model weights
python scripts/download_weights.py 
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

### 3. Core Backend API
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head # Run database/PostGIS migrations
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Frontend UI
```bash
cd frontend
npm install
npm run dev
```

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/SpatialAlgorithm`)
3. Commit your changes (`git commit -m 'Add new carrying capacity algorithm'`)
4. Push to the branch (`git push origin feature/SpatialAlgorithm`)
5. Open a Pull Request

---

## Contact

**Project Lead:** Hardik Gupta  
**Email:** [tatsahayk@gmail.com](mailto:tatsahayk@gmail.com)  
**Live Platform:** [www.tatsahayk.in](http://www.tatsahayk.in)

---

<div align="center">

### Star this repository if you find it useful!

---

*"Building resilient futures through spatial intelligence."*

</div>
