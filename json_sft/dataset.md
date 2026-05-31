# Dataset Acquisition Guide

> This document summarizes the sources, download methods, and basic information for all datasets involved in this project.
> Datasets are listed in index order as defined in `source_datasets.md`.

---

## Datasets by Index

### [01] LLVIP — Visible-Infrared Paired Dataset for Low-light Vision

| Attribute | Details |
|-----------|---------|
| **Task** | Low-light pedestrian detection |
| **Scale** | 15,488 RGB-IR pairs (30,976 images total) |
| **Source** | ICCV 2021 Workshop |
| **Project Dir** | `1-LLVIP/` |

**How to obtain:**
- Official homepage: <https://bupt-ai-cz.github.io/LLVIP/>
- Fill in your name, email, affiliation, and agree to the usage terms on the homepage; a download link will be sent within ~10 seconds
- If issues arise, contact the author: <czhu@bupt.edu.cn>
- GitHub repository (code and pretrained models): <https://github.com/bupt-ai-cz/LLVIP>

**Paper:**
> Jia, X., et al. "LLVIP: A Visible-infrared Paired Dataset for Low-light Vision." ICCVW 2021. [arXiv:2108.10831](https://arxiv.org/abs/2108.10831)

---

### [02] KAIST — Multispectral Pedestrian Detection Benchmark

| Attribute | Details |
|-----------|---------|
| **Task** | Multispectral pedestrian detection |
| **Scale** | ~95,000 RGB-Thermal image pairs |
| **Source** | CVPR 2015 |
| **Project Dir** | `2-KAIST/` |

**How to obtain:**
- Official homepage: <https://soonminhwang.github.io/rgbt-ped-detection/>
- GitHub repository: <https://github.com/soonminhwang/rgbt-ped-detection>
- **Google Drive (recommended):** Use `gdown` to download
  ```bash
  pip install gdown
  # Full dataset (36.32 GB)
  gdown 1sBcAmFqNJmNMBZdMtKmO2X4BRjKPyKMc
  # Preview set (1.44 GB)
  gdown 11nhHpmuh2FUjrLNfGs51R2Mqqy1GTjY8
  ```
- Alternatively, use the scripts in the repository to download from OneDrive

**Paper:**
> Hwang, S., et al. "Multispectral Pedestrian Detection: Benchmark Dataset and Baseline." CVPR 2015.

---

### [03] M3FD — Multi-scenario Multi-Modality Benchmark

| Attribute | Details |
|-----------|---------|
| **Task** | Infrared-Visible image fusion and object detection (6 classes) |
| **Scale** | 4,200 + 300 RGB-IR pairs, 34,407 bounding boxes |
| **Source** | CVPR 2022 (Oral) |
| **Project Dir** | `3-M3FD/` |

**How to obtain:**
- GitHub repository (with Google Drive / Baidu Netdisk links): <https://github.com/JinyuanLiu-CV/TarDAL>
- Check the README for the latest download links

**Paper:**
> Liu, J., et al. "Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection." CVPR 2022.

---

### [04] VEDAI — Vehicle Detection in Aerial Imagery

| Attribute | Details |
|-----------|---------|
| **Task** | Remote sensing vehicle detection (9 classes, oriented bounding boxes) |
| **Scale** | 1,210 images |
| **Source** | University of Caen, 2015 |
| **Project Dir** | `4-VEDAI/` |

**How to obtain:**
- Official download: <https://downloads.greyc.fr/vedai/>

---

### [06] LSOTB-TIR — Large-Scale High-Diversity Thermal Infrared Object Tracking Benchmark

| Attribute | Details |
|-----------|---------|
| **Task** | Thermal infrared object tracking (47 classes) |
| **Scale** | 1,400 sequences, 600K+ frames, 730K+ bounding boxes |
| **Source** | ACM MM 2020 |
| **Project Dir** | `6-LSOTB-TIR/` |

**How to obtain:**
- GitHub repository: <https://github.com/QiaoLiuHit/LSOTB-TIR>
- International users: TeraBox download
- China users: Baidu Netdisk (access code: `dr3i`)
- Includes MATLAB evaluation toolkit

**Paper:**
> Liu, Q., et al. "LSOTB-TIR: A Large-Scale High-Diversity Thermal Infrared Object Tracking Benchmark." ACM MM 2020.

---

### [07] RGBT234 — RGBT234 Tracking Benchmark

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-T object tracking |
| **Scale** | 234 video sequences, ~116.7K frames |
| **Source** | Anhui University, Pattern Recognition 2019 |
| **Project Dir** | `7-RGBT234/` |

**How to obtain:**
- Unified entry GitHub repository: <https://github.com/xuboyue1999/RGBT-Tracking>
- See `rgbt234.md` in the repository for specific download links

**Paper:**
> Li, C., et al. "RGB-T Object Tracking: Benchmark and Baseline." PR 2019.

---

### [08] LasHeR — Large-scale High-diversity Benchmark for RGBT Tracking

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-T object tracking |
| **Scale** | 1,224 video sequences, 730K+ frames |
| **Source** | Anhui University, IEEE TIP 2022 |
| **Project Dir** | `8-LasHeR/` |

**How to obtain:**
- GitHub repository: <https://github.com/BUGPLEASEOUT/LasHeR>
- Alternate: <https://github.com/mmic-lcl/Datasets-and-benchmark-code>
- Also available via: <https://github.com/xuboyue1999/RGBT-Tracking>

**Paper:**
> Li, C., et al. "LasHeR: A Large-Scale High-Diversity Benchmark for RGBT Tracking." IEEE TIP 2022. [arXiv:2104.13202](https://arxiv.org/abs/2104.13202)

---

### [09] VTUAV — Visible-Thermal UAV Tracking Benchmark

| Attribute | Details |
|-----------|---------|
| **Task** | UAV-perspective RGB-T tracking |
| **Scale** | 1.7M frames across multiple sequences |
| **Source** | Anhui University |
| **Project Dir** | `9-VTUAV/` |

**How to obtain:**
- Via the unified RGB-T Tracking repository: <https://github.com/xuboyue1999/RGBT-Tracking>
- Contact the Li group at Anhui University

---

### [10] MFNet — Multi-spectral Fusion Network

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-Thermal urban scene semantic segmentation (8 classes) |
| **Scale** | 1,569 image pairs (820 train + 749 test) |
| **Source** | IROS 2017 |
| **Project Dir** | `10-MFNet/` |

**How to obtain:**
- GitHub repository (PyTorch implementation): <https://github.com/haqishen/MFNet-pytorch> (download link in README)
- Data captured from a vehicle-mounted multispectral camera in urban scenes

**Paper:**
> Ha, Q., et al. "MFNet: Towards Real-time Semantic Segmentation for Autonomous Vehicles with Multi-Spectral Scenes." IROS 2017.

---

### [11] IRSTD-1k — Infrared Small Target Detection 1k

| Attribute | Details |
|-----------|---------|
| **Task** | Infrared small target detection |
| **Scale** | 1,000 images |
| **Source** | CVPR 2022 |
| **Project Dir** | `11-IRSTD-1k/` |

**How to obtain:**
- GitHub repository: <https://github.com/RuiZhang97/ISNet>

**Paper:**
> Zhang, R., et al. "ISNet: Shape Matters for Infrared Small Target Detection." CVPR 2022.

---

### [12] SIRST-AUG — Augmented SIRST Dataset

| Attribute | Details |
|-----------|---------|
| **Task** | Infrared small target detection |
| **Scale** | 8,500 images (augmented) |
| **Source** | CVPR 2022 |
| **Project Dir** | `12-SIRST-AUG/` |

**How to obtain:**
- Available via the ISNet repository: <https://github.com/RuiZhang97/ISNet>

**Paper:**
> Zhang, R., et al. "ISNet: Shape Matters for Infrared Small Target Detection." CVPR 2022.

---

### [13] BU-TIV — Thermal Infrared Video Benchmark

| Attribute | Details |
|-----------|---------|
| **Task** | Thermal infrared vehicle detection and speed measurement |
| **Scale** | ~60,000 frames |
| **Project Dir** | `13-BU-TIV/` |

**How to obtain:**
- Contact the corresponding paper authors

---

### [14] VisDrone-DroneVehicle

| Attribute | Details |
|-----------|---------|
| **Full Name** | DroneVehicle: Drone-based RGB-Infrared Cross-Modality Vehicle Detection |
| **Task** | UAV-perspective RGB-T vehicle detection (5 classes, oriented bounding boxes) |
| **Scale** | 28,439 RGB-IR pairs, ~953,000 annotated instances |
| **Source** | Tianjin University / VisDrone |
| **Project Dir** | `14-VisDrone-DroneVehicle/` |

**How to obtain:**
- GitHub repository: <https://github.com/VisDrone/DroneVehicle>
- Images contain white borders (resolution 840x712); crop to 640x512 before training

**Paper:**
> Sun, Y., et al. "Drone-based RGB-Infrared Cross-Modality Vehicle Detection via Uncertainty-Aware Learning." IEEE TCSVT 2022.

---

### [16] MassMIND

| Attribute | Details |
|-----------|---------|
| **Task** | Maritime surveillance / object detection |
| **Scale** | ~2,900 images |
| **Project Dir** | `16-MassMIND/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [17] ISDD

| Attribute | Details |
|-----------|---------|
| **Task** | Infrared ship detection |
| **Scale** | ~1,300 images |
| **Project Dir** | `17-ISDD/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [18] CDFAG

| Attribute | Details |
|-----------|---------|
| **Task** | Cross-domain facial attribute generation |
| **Scale** | ~88,000 images |
| **Project Dir** | `18-CDFAG/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [19] WideIRSTD — Wide Infrared Small Target Detection

| Attribute | Details |
|-----------|---------|
| **Task** | Infrared small target detection |
| **Scale** | ~9,000 images |
| **Project Dir** | `19-WideIRSTD/` |

**How to obtain:**
- GitHub repository: <https://github.com/XinyiYing/WideIRSTD-Dataset>

---

### [20] DMIST — Dual-Modal Infrared Small Target

| Attribute | Details |
|-----------|---------|
| **Task** | Infrared small target detection |
| **Scale** | ~9,000 images |
| **Project Dir** | `20-DMIST/` |

**How to obtain:**
- Contact the corresponding paper authors

---

### [21] JU-VNT

| Attribute | Details |
|-----------|---------|
| **Task** | Visible-NIR thermal scene analysis |
| **Scale** | ~2,600 image pairs |
| **Project Dir** | `21-JU-VNT/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [22] POP

| Attribute | Details |
|-----------|---------|
| **Task** | Pedestrian occlusion / detection |
| **Scale** | ~7,800 images |
| **Project Dir** | `22-POP/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [23] RGBTCrowdCounting (RGBT-CC) — RGB-T Crowd Counting

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-T crowd counting |
| **Scale** | 2,030 RGB-Thermal image pairs, 138,389 annotated persons |
| **Source** | CVPR 2021 |
| **Project Dir** | `23-RGBTCrowdCounting/` |

**How to obtain:**
- GitHub repository: <https://github.com/chen-judge/RGBTCrowdCounting>
- Dropbox link / Baidu Netdisk (access code: `RGBT`)

**Paper:**
> Liu, L., et al. "Cross-Modal Collaborative Representation Learning and a Large-Scale RGBT Benchmark for Crowd Counting." CVPR 2021. [arXiv:2012.04529](https://arxiv.org/abs/2012.04529)

---

### [24] VT5000 — RGB-T Tracking (5,000 sequences)

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-T object tracking |
| **Scale** | 5,000 video sequences |
| **Source** | Anhui University |
| **Project Dir** | `24-VT5000/` |

**How to obtain:**
- Unified entry: <https://github.com/xuboyue1999/RGBT-Tracking>

---

### [27] Industry

| Attribute | Details |
|-----------|---------|
| **Task** | Industrial scene inspection |
| **Scale** | ~400 images |
| **Project Dir** | `27-Industry/` |

**How to obtain:**
- Refer to the corresponding source or contact the dataset publisher

---

### [28] VT1000 — RGB-T Tracking (1,000 sequences)

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-T object tracking |
| **Scale** | 1,000 video sequences |
| **Source** | Anhui University |
| **Project Dir** | `28-VT1000/` |

**How to obtain:**
- Unified entry: <https://github.com/xuboyue1999/RGBT-Tracking>

---

### [29] VT821 — RGB-T Tracking (821 sequences)

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-T object tracking |
| **Scale** | 821 video sequences |
| **Source** | Anhui University |
| **Project Dir** | `29-VT821/` |

**How to obtain:**
- Unified entry: <https://github.com/xuboyue1999/RGBT-Tracking>

---

### [30] UVT2000 — Unmanned Vehicle Thermal Tracking

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-T object tracking |
| **Scale** | 2,000 video sequences |
| **Source** | Anhui University |
| **Project Dir** | `30-UVT2000/` |

**How to obtain:**
- Unified entry: <https://github.com/xuboyue1999/RGBT-Tracking>

---

### [31] FLIR — Teledyne FLIR Starter Thermal Dataset

| Attribute | Details |
|-----------|---------|
| **Task** | Autonomous driving object detection (15 classes) |
| **Scale** | 26,442 frames (RGB + Thermal) |
| **Source** | Teledyne FLIR |
| **Project Dir** | `31-FLIR/` |

**How to obtain:**
- Official download page (form required): <https://prep.flir.eu/oem/adas/adas-dataset-form/>
- Chinese page: <https://oem.flir.com/zh-cn/solutions/automotive/adas-dataset-form/>
- Kaggle mirror: <https://www.kaggle.com/datasets/samdazel/teledyne-flir-adas-thermal-dataset-v2>
- **Note:** RGB and thermal images are temporally synchronized but have different fields of view; pixel-level alignment must be performed manually

**Paper:**
> Teledyne FLIR. "Free FLIR Thermal Dataset for Algorithm Training." 2018.

---

### [51] RGBNIR — RGB-NIR Scene Dataset

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-NIR scene classification (9 classes) |
| **Scale** | 477 image pairs |
| **Source** | EPFL IVRL Lab |
| **Project Dir** | `51-RGBNIR/` |

**How to obtain:**
- Official download: <https://www.epfl.ch/labs/ivrl/research/downloads/rgb-nir-scene-dataset/>
- Captured with a modified DSLR camera; RGB and NIR images are pre-aligned

**Paper:**
> Brown, M., et al. "Multi-spectral SIFT for Scene Category Recognition." CVPR 2011.

---

### [52] UAV_RGB-T_2400

| Attribute | Details |
|-----------|---------|
| **Task** | UAV-perspective RGB-T object tracking/detection |
| **Scale** | 2,400 image pairs |
| **Project Dir** | `52-UAV_RGB-T_2400/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [53] LLCM — Low-Light Cross-Modality Dataset

| Attribute | Details |
|-----------|---------|
| **Task** | Low-light RGB-IR person re-identification |
| **Scale** | 1,064 IDs, 46,767 bounding boxes, 9 RGB/IR cameras |
| **Source** | Xiamen University, CVPR 2023 |
| **Project Dir** | `53-LLCM/` |

**How to obtain:**
- GitHub repository: <https://github.com/ZYK100/LLCM>
- Download and sign the [LLCM Dataset Release Agreement (PDF)](https://github.com/ZYK100/LLCM/blob/main/LLCM%20Dataset%20Agreement/LLCM%20DATASET%20RELEASE%20AGREEMENT.pdf)
- Email the signed agreement to: <zhangyk@stu.xmu.edu.cn>
- A download link will be provided after approval

**Paper:**
> Zhang, Y., et al. "Diverse Embedding Expansion Network and Low-Light Cross-Modality Benchmark for Visible-Infrared Person Re-identification." CVPR 2023.

---

### [54] RegDB — Dongguk Body-based Person Recognition Database

| Attribute | Details |
|-----------|---------|
| **Task** | Visible-Thermal person re-identification |
| **Scale** | 412 IDs, 10 RGB + 10 IR images per person |
| **Source** | Dongguk University, Sensors 2017 |
| **Project Dir** | `54-RegDB/` |

**How to obtain:**
- Visit the official website and submit a copyright application form
- Or send an email to <mangye16@gmail.com> to request a download link
- Standard evaluation protocol: 206 ID train / 206 ID test, 10 random trials

**Paper:**
> Nguyen, D.T., et al. "Person Recognition System Based on a Combination of Body Images from Visible Light and Thermal Cameras." Sensors, 2017.

---

### [55] SYSU-MM01 — RGB-IR Person Re-Identification

| Attribute | Details |
|-----------|---------|
| **Task** | Visible-Infrared cross-modality person re-identification |
| **Scale** | 491 IDs, 30,071 RGB images + 15,792 IR images |
| **Source** | Sun Yat-sen University, ICCV 2017 / IJCV 2020 |
| **Project Dir** | `55-SYSU-MM01/` |

**How to obtain:**
- GitHub repository: <https://github.com/wuancong/SYSU-MM01>
- Download and sign the dataset release agreement, send to <wuanc@mail.sysu.edu.cn>
- A download link will be provided after approval

**Paper:**
> Wu, A., et al. "RGB-Infrared Cross-Modality Person Re-Identification." ICCV 2017 / IJCV 2020.

---

### [56] ThermalWorld — Multispectral Person Re-Identification

| Attribute | Details |
|-----------|---------|
| **Task** | Thermal-Visible person re-identification |
| **Scale** | Training subset publicly available; 8,100 image pairs total |
| **Source** | ThermalGAN (WACV 2018) |
| **Project Dir** | `56-ThermalWorld/` |

**How to obtain:**
- ThermalGAN GitHub Issues page: <https://github.com/vlkniaz/ThermalGAN/issues>
- MREiD-UCD-CCD repository may provide a Google Drive link: <https://github.com/art2611/mreid-ucd-ccd>
- **Note:** The full dataset is not publicly available; currently only the training subset is accessible

---

### [57] solar_cell_EL_image

| Attribute | Details |
|-----------|---------|
| **Task** | Solar cell electroluminescence (EL) image analysis |
| **Scale** | ~36,500 images |
| **Project Dir** | `57-solar_cell_EL_image/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [58] sirst_aug

| Attribute | Details |
|-----------|---------|
| **Task** | Infrared small target detection (augmented) |
| **Scale** | ~18,100 images |
| **Project Dir** | `58-sirst_aug/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher
- May overlap with SIRST-AUG (index 12)

---

### [59] tirsequences

| Attribute | Details |
|-----------|---------|
| **Task** | Thermal infrared image sequences |
| **Scale** | ~30,000 images |
| **Project Dir** | `59-tirsequences/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [60] DroneRGBT — Drone-based RGB-T Crowd Counting

| Attribute | Details |
|-----------|---------|
| **Task** | UAV-perspective RGB-T crowd counting |
| **Scale** | 3,600 RGB-Thermal image pairs |
| **Source** | VisDrone |
| **Project Dir** | `60-DroneRGBT/` |

**How to obtain:**
- GitHub repository: <https://github.com/VisDrone/DroneRGBT>
- Baidu Netdisk (access code: `1895`)

---

### [61] UVT20K — Unmanned Vehicle Thermal Tracking (20K)

| Attribute | Details |
|-----------|---------|
| **Task** | RGB-T object tracking |
| **Scale** | 20,000 video sequences |
| **Source** | Anhui University |
| **Project Dir** | `61-UVT20K/` |

**How to obtain:**
- Unified entry: <https://github.com/xuboyue1999/RGBT-Tracking>

---

### [62] time-sensitive

| Attribute | Details |
|-----------|---------|
| **Task** | Time-sensitive visual understanding |
| **Scale** | ~21,800 images |
| **Project Dir** | `62-time-sensitive/` |

**How to obtain:**
- Refer to the corresponding academic paper or contact the dataset publisher

---

### [63] FLIR_ADAS — Teledyne FLIR ADAS Thermal Dataset v2

| Attribute | Details |
|-----------|---------|
| **Task** | ADAS object detection with COCO-format annotations (15 classes) |
| **Scale** | 26,442 frames, 520,000+ bounding boxes |
| **Source** | Teledyne FLIR (2022) |
| **Project Dir** | `63-FLIR_ADAS/` |

**How to obtain:**
- Same official entry point as FLIR: <https://prep.flir.eu/oem/adas/adas-dataset-form/>
- Kaggle mirror: <https://www.kaggle.com/datasets/samdazel/teledyne-flir-adas-thermal-dataset-v2>
- Contains `coco.json` files in MSCOCO annotation format

---

## Summary Table (by Index)

| Index | Dataset | Task Type | Scale | Public Access |
|:-----:|---------|-----------|-------|:-------------:|
| 01 | LLVIP | RGB-T Pedestrian Detection | 15,488 pairs | ✅ Web form |
| 02 | KAIST | Multispectral Pedestrian Detection | 95,000 pairs | ✅ Google Drive |
| 03 | M3FD | RGB-T Fusion + Detection | 4,200 pairs | ✅ Google Drive |
| 04 | VEDAI | Remote Sensing Vehicle Detection | 1,210 images | ✅ Direct download |
| 06 | LSOTB-TIR | Thermal Infrared Tracking | 1,400 sequences | ✅ GitHub |
| 07 | RGBT234 | RGB-T Tracking | 234 sequences | ✅ GitHub |
| 08 | LasHeR | RGB-T Tracking | 1,224 sequences | ✅ GitHub |
| 09 | VTUAV | UAV RGB-T Tracking | 1.7M frames | ✅ GitHub |
| 10 | MFNet | RGB-T Semantic Segmentation | 1,569 pairs | ✅ GitHub |
| 11 | IRSTD-1k | Infrared Small Target Detection | 1,000 images | ✅ GitHub |
| 12 | SIRST-AUG | Infrared Small Target Detection | 8,500 images | ✅ GitHub |
| 13 | BU-TIV | Thermal Speed Measurement | 60K frames | ⚠️ Contact author |
| 14 | DroneVehicle | UAV RGB-T Vehicle Detection | 28,439 pairs | ✅ GitHub |
| 16 | MassMIND | Maritime Surveillance | 2,900 images | ⚠️ Contact author |
| 17 | ISDD | Infrared Ship Detection | 1,300 images | ⚠️ Contact author |
| 18 | CDFAG | Cross-Domain Facial Generation | 88,000 images | ⚠️ Contact author |
| 19 | WideIRSTD | Infrared Small Target Detection | 9,000 images | ✅ GitHub |
| 20 | DMIST | Infrared Small Target Detection | 9,000 images | ⚠️ Contact author |
| 21 | JU-VNT | Visible-NIR Thermal | 2,600 pairs | ⚠️ Contact author |
| 22 | POP | Pedestrian Occlusion | 7,800 images | ⚠️ Contact author |
| 23 | RGBT-CC | RGB-T Crowd Counting | 2,030 pairs | ✅ Dropbox/Netdisk |
| 24 | VT5000 | RGB-T Tracking | 5,000 sequences | ✅ GitHub |
| 27 | Industry | Industrial Inspection | 400 images | ⚠️ Contact author |
| 28 | VT1000 | RGB-T Tracking | 1,000 sequences | ✅ GitHub |
| 29 | VT821 | RGB-T Tracking | 821 sequences | ✅ GitHub |
| 30 | UVT2000 | RGB-T Tracking | 2,000 sequences | ✅ GitHub |
| 31 | FLIR | Autonomous Driving Detection | 26,442 frames | ✅ Web form |
| 51 | RGBNIR | RGB-NIR Scene Classification | 477 pairs | ✅ Direct download |
| 52 | UAV_RGB-T_2400 | RGB-T UAV | 2,400 pairs | ⚠️ Contact author |
| 53 | LLCM | RGB-IR Person ReID | 1,064 IDs | ✅ Signed agreement |
| 54 | RegDB | RGB-IR Person ReID | 412 IDs | ✅ Signed agreement |
| 55 | SYSU-MM01 | RGB-IR Person ReID | 491 IDs | ✅ Signed agreement |
| 56 | ThermalWorld | RGB-IR ReID | 8,100 pairs | ⚠️ Partially public |
| 57 | solar_cell_EL_image | Solar Cell EL Analysis | 36,500 images | ⚠️ Contact author |
| 58 | sirst_aug | Infrared Small Target Detection | 18,100 images | ⚠️ Contact author |
| 59 | tirsequences | Thermal IR Sequences | 30,000 images | ⚠️ Contact author |
| 60 | DroneRGBT | UAV RGB-T Crowd Counting | 3,600 pairs | ✅ GitHub |
| 61 | UVT20K | RGB-T Tracking | 20,000 sequences | ✅ GitHub |
| 62 | time-sensitive | Time-Sensitive Vision | 21,800 images | ⚠️ Contact author |
| 63 | FLIR_ADAS | ADAS Object Detection | 26,442 frames | ✅ Web form |

---

## Important Notes

1. **License restrictions:** All datasets are for academic research use only. Commercial use is prohibited.
2. **Citation requirements:** Please cite the corresponding original papers when using any dataset.
3. **Privacy compliance:** Datasets containing human subjects (e.g., SYSU-MM01, RegDB) have obtained participant privacy authorizations. Do not use the data for purposes unrelated to the original research.
4. **Link validity:** Download links may change over time. It is recommended to check each dataset's GitHub repository or official homepage for the latest download methods.

---
