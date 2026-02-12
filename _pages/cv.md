---
layout: cv-layout
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<div class="cv-container">

  <!-- Debug -->


  <!-- Appointments -->
  <div class="cv-section">
    <h2>Appointments</h2>
    {% assign entries = site.data.cv.Experience %}
    {% include cv/experience.liquid %}
  </div>

  <!-- Education -->
  <div class="cv-section">
    <h2>Education</h2>
    {% assign entries = site.data.cv.Education %}
    {% include cv/education.liquid %}
  </div>

  <!-- Grants, Fellowships & Awards -->
  <div class="cv-section">
    <h2>Grants, Fellowships & Awards</h2>
    {% assign entries = site.data.cv.Awards %}
    {% include cv/awards.liquid %}
  </div>

  <!-- Service -->
  <div class="cv-section">
    <h2>Service</h2>
    <ul class="cv-list">
      {% for item in site.data.cv.Service %}
      <li class="cv-item">
        <div class="cv-item-header">
          <div class="cv-item-title">{{ item.name }}</div>
        </div>
        <div class="cv-item-detail">{{ item.summary }}</div>
      </li>
      {% endfor %}
    </ul>
  </div>

  <!-- Publications -->
  <div class="cv-section">
    <h2>Publications</h2>
    <ul class="cv-list">
      {% for post in site.publications reversed %}
        {% include archive-single-cv.html %}
      {% endfor %}
    </ul>
  </div>
  
  <!-- Talks -->
  <div class="cv-section">
    <h2>Talks</h2>
    <ul class="cv-list">
      {% for post in site.talks reversed %}
        {% include archive-single-talk-cv.html  %}
      {% endfor %}
    </ul>
  </div>
  
  <!-- Teaching -->
  <div class="cv-section">
    <h2>Teaching</h2>
    <ul class="cv-list">
      {% for post in site.teaching reversed %}
        {% include archive-single-cv.html %}
      {% endfor %}
    </ul>
  </div>

</div>
