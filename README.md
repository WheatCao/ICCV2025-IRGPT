# [ICCV2025] IRGPT: A Large-scale Real-world Infrared Image Dataset

Official repository for the **IR-TD dataset** from the ICCV 2025 paper:  
**"IRGPT: Understanding Real-world Infrared Image with Bi-cross-modal Curriculum on Large-scale Benchmark"**

---

## Dataset Overview

**IR-TD** (InfraRed-Text Dataset) is the first large-scale, real-world infrared image-text benchmark, curated for advancing multi-modal vision-language research in the infrared domain.  
It is released together with our ICCV 2025 paper:  
**IRGPT: Understanding Real-world Infrared Image with Bi-cross-modal Curriculum on Large-scale Benchmark**.

### Key Statistics

- **Total samples:** Over **260,000** real infrared–text pairs
- **Sources:** Aggregated from **63** publicly available datasets (e.g., LLVIP, KAIST, FLIR, VTUAV, RGBT234, LasHeR, etc.)
- **Annotations:**  
  - Detailed image captions (LLM-generated and human-refined)  
  - Rich question-answer (QA) pairs (LLM & rule-based)  
  - Multi-task labels for 9 core tasks (see below)

### Data Composition

IR-TD is organized into three main subsets:
- **Pre-training Subset:** 190K+ pairs for large-scale model pretraining (image-text pairs)
- **Instruction (Fine-tuning) Subset:** 33K+ samples for instruction-following and Q&A training
- **Benchmark Subset:** 37K+ samples for multi-task evaluation

### Task Coverage

The IR-TD benchmark supports the following **9 representative tasks**:

| Task                | Description                                                |
|---------------------|-----------------------------------------------------------|
| Recognition         | Multi-choice object/category recognition                   |
| Grounding           | Object localization with bounding boxes                    |
| Location            | Return coordinates of all instances of a category          |
| Relationship        | Spatial relationship reasoning (left/right/front/back/etc) |
| Re-ID               | Person re-identification (cross-scene/camera)              |
| Security            | Identify categories *absent* from the image                |
| Aerial Counting     | Vehicle counting from UAV imagery                          |
| Pedestrian Counting | People counting in crowd scenes                            |
| Scene               | Scene classification (urban/field/forest, etc.)            |

Annotations are generated via a combination of LLM-based natural language description, rule-based QA pair construction, and standardized templates for each task.

### Source Diversity

IR-TD merges and re-annotates images from diverse open datasets, covering:
- Urban, rural, aerial, surveillance, night, industrial scenes
- Representative sources:  
  - **LLVIP** (15.5K), **KAIST** (95.3K), **FLIR** (10K), **VTUAV** (1.7M), **RGBT234** (234K), **LasHeR** (734.8K), **MFNet**, **IRSTD-1k**, **SIRST-AUG**, and more  
- See [docs/source_datasets.md](docs/source_datasets.md) for full list

Unaligned visible-infrared pairs are processed with semantic cropping to ensure cross-modal alignment.

### Annotation Examples

```json
{
  "description": "A nighttime street with several parked cars and a streetlight. No visible people.",
  "qa_pairs": [
    {"question": "How many cars are present?", "answer": "3"},
    {"question": "Is it daytime or nighttime?", "answer": "Nighttime"}
  ],
  "bounding_boxes": [
    {"category": "car", "bbox": [x1, y1, x2, y2]}
  ],
  "scene": "urban"
}

