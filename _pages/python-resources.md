---
layout: archive
title: "Scientific Python for Geosciences"
permalink: /teaching/python-resources/
author_profile: false
header:
  overlay_filter: 0.5
  overlay_image: featured_scientific_python.png
---

<style>
  .btn {
    text-decoration: none !important;
  }
</style>

{% include base_path %}

Welcome to the course on **Scientific Python for Geosciences**. This course will teach you basics of data analysis with pandas and xarray for geoscientific data analysis. This page centralizes my teaching materials, including slides and exercises. The content was developped thanks to CNRS formation and the Atelier Numérique de l'Observatoire Midi-Pyrénées. The material was developped in collaboration with Adrien Garinet.

<div class="resource-main-actions" style="display: flex; gap: 1.5rem; margin-bottom: 2rem; flex-wrap: wrap; align-items: stretch;">
  <a href="https://zenodo.org/records/18662963" class="btn btn--info btn--x-large" target="_blank" rel="noopener noreferrer" style="margin-bottom: 0; flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 2rem 1rem; min-height: 180px; min-width: 200px; background-color: #11999e !important; border-color: #11999e !important;">
    <i class="fas fa-archive" style="font-size: 2.5rem; margin-bottom: 1rem;"></i>
    <span>Download full<br>Zenodo Archive</span>
  </a>
  <a href="https://mybinder.org/v2/gh/rguilcas/python-geosciences/main?labpath=Welcome.ipynb" class="btn btn--warning btn--x-large" target="_blank" rel="noopener noreferrer" style="margin-bottom: 0; flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 2rem 1rem; min-height: 180px; min-width: 200px; background-color: #e67e22 !important; border-color: #e67e22 !important;">
    <i class="fas fa-rocket" style="font-size: 2.5rem; margin-bottom: 1rem;"></i>
    <span>Launch<br>Jupyter Hub (Binder)</span>
  </a>
</div>

<div class="resource-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin-bottom: 3rem;">

<article class="resource-block-v" style="display: flex; flex-direction: column; padding: 1.5rem; background: var(--global-bg-color); border: 1px solid var(--global-border-color); border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
<div class="archive__item-teaser" style="margin-bottom: 1.5rem; text-align: center; height: 100px; display: flex; align-items: center; justify-content: center;">
  <img src="{{ base_path }}/images/python_logo.png" alt="Python Logo" style="max-height: 100%; width: auto;">
</div>
<div class="archive__item-content" markdown="1">
### 1. General Introduction
Basics of the Python ecosystem.

**<i class="fas fa-file-powerpoint" style="color: #d24726;"></i> Slides:**
[PDF](https://github.com/rguilcas/python-geosciences/blob/main/slides/General%20introduction.pdf){: .btn .btn--info .btn--small style="background-color: #5d85a6 !important;" target="_blank"}
[PPTX](https://github.com/rguilcas/python-geosciences/blob/main/slides/General%20introduction.pptx){: .btn .btn--info .btn--small style="background-color: #5d85a6 !important;" target="_blank"}

**<i class="fab fa-youtube" style="color: #ff0000;"></i> Recordings:**
<a href="https://www.youtube.com/watch?v=fxmhKIxFZhM" class="btn btn--danger btn--small" target="_blank">Watch</a> Intro
</div>
</article>

<article class="resource-block-v" style="display: flex; flex-direction: column; padding: 1.5rem; background: var(--global-bg-color); border: 1px solid var(--global-border-color); border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
<div class="archive__item-teaser" style="margin-bottom: 1.5rem; text-align: center; height: 100px; display: flex; align-items: center; justify-content: center;">
  <img src="{{ base_path }}/images/pandas_logo.png" alt="Pandas Logo" style="max-height: 100%; width: auto;">
</div>
<div class="archive__item-content" markdown="1">
### 2. Data Analysis with Pandas
Mastering tabular data processing.

**<i class="fas fa-file-powerpoint" style="color: #d24726;"></i> Slides:**
[PDF](https://github.com/rguilcas/python-geosciences/blob/main/slides/Introduction%20to%20pandas.pdf){: .btn .btn--info .btn--small style="background-color: #5d85a6 !important;" target="_blank"}
[PPTX](https://github.com/rguilcas/python-geosciences/blob/main/slides/Introduction%20to%20pandas.pptx){: .btn .btn--info .btn--small style="background-color: #5d85a6 !important;" target="_blank"}

**<i class="fab fa-youtube" style="color: #ff0000;"></i> Recordings:**
<div style="display: flex; flex-direction: column; gap: 0.5rem; align-items: flex-start; margin-top: 0.5rem;">
  <div style="display: flex; align-items: center; gap: 0.5rem;"><a href="https://www.youtube.com/watch?v=fxmhKIxFZhM&t=800s" class="btn btn--danger btn--small" target="_blank">Pt 1</a> <span>Intro</span></div>
  <div style="display: flex; align-items: center; gap: 0.5rem;"><a href="https://www.youtube.com/watch?v=i28CBhRdCk8&t=13s" class="btn btn--danger btn--small" target="_blank">Pt 2</a> <span>Analyses</span></div>
  <div style="display: flex; align-items: center; gap: 0.5rem;"><a href="https://www.youtube.com/watch?v=yOIBD5c3q60" class="btn btn--danger btn--small" target="_blank">Pt 3</a> <span>Plotting</span></div>
  <div style="display: flex; align-items: center; gap: 0.5rem;"><a href="https://www.youtube.com/watch?v=_MshkMjiEBc&t=5s" class="btn btn--danger btn--small" target="_blank">Pt 4</a> <span>Timeseries</span></div>
</div>
</div>
</article>

<article class="resource-block-v" style="display: flex; flex-direction: column; padding: 1.5rem; background: var(--global-bg-color); border: 1px solid var(--global-border-color); border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
<div class="archive__item-teaser" style="margin-bottom: 1.5rem; text-align: center; height: 100px; display: flex; align-items: center; justify-content: center;">
  <img src="{{ base_path }}/images/xarray_logo.png" alt="Xarray Logo" style="max-height: 100%; width: auto;">
</div>
<div class="archive__item-content" markdown="1">
### 3. Arrays with Xarray & Dask
N-dimensional arrays and parallel computing.

**<i class="fas fa-file-powerpoint" style="color: #d24726;"></i> Slides:**
[PDF](https://github.com/rguilcas/python-geosciences/blob/main/slides/Introduction%20to%20xarray.pdf){: .btn .btn--info .btn--small style="background-color: #5d85a6 !important;" target="_blank"}
[PPTX](https://github.com/rguilcas/python-geosciences/blob/main/slides/Introduction%20to%20xarray.pptx){: .btn .btn--info .btn--small style="background-color: #5d85a6 !important;" target="_blank"}

**<i class="fab fa-youtube" style="color: #ff0000;"></i> Recordings:**
<div style="display: flex; flex-direction: column; gap: 0.5rem; align-items: flex-start; margin-top: 0.5rem;">
  <div style="display: flex; align-items: center; gap: 0.5rem;"><a href="https://www.youtube.com/watch?v=yK_0lO_vfog" class="btn btn--danger btn--small" target="_blank">Pt 1</a> <span>Intro</span></div>
  <div style="display: flex; align-items: center; gap: 0.5rem;"><a href="https://www.youtube.com/watch?v=f9SYuBDDi5A&t=897s" class="btn btn--danger btn--small" target="_blank">Pt 2</a> <span>Analyses</span></div>
  <div style="display: flex; align-items: center; gap: 0.5rem;"><a href="https://www.youtube.com/watch?v=KgUE5P4-Qt8" class="btn btn--danger btn--small" target="_blank">Pt 3</a> <span>Plotting</span></div>
  <div style="display: flex; align-items: center; gap: 0.5rem;"><a href="https://www.youtube.com/watch?v=LfryRgpfFTo" class="btn btn--danger btn--small" target="_blank">Pt 4</a> <span>Dask Lecture</span></div>
</div>
</div>
</article>

</div>



---


