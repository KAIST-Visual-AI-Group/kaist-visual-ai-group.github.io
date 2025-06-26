---
hide:
  - navigation
  - toc
---

<style>
p { text-align: justify; }

.md-typeset h2 {
    margin: 0.5em 0 0 0;
}

.container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 1rem;
}

.swiper {
    width: 100%;
    height: 100%;
}

.swiper-slide {
    margin-bottom: 1em;
}

.news {
    justify-items: center;
    align-items: center;
}

.gallery {
    justify-items: center;
    align-items: center;
}

.gallery h2 {
    margin: 0.5em 0 0.5em 0;
}

@media only screen and (max-width: 600px) {
    .container {
        grid-template-columns: 1fr;
    }
}
</style>


{% set professor = people.professor %}


# {{ config.site_name }}
The KAIST Visual AI Group, led by <a href="{{ professor.web }}" target="_blank">__{{ professor.name }}__</a>, conducts research on advancing technologies for generating, processing, and analyzing diverse visual data. Our work spans areas such as machine learning, computer vision, and computer graphics.
<!-- Link Swiper's CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

<!-- Research Highlights -->
<div class="swiper research-highlights-swiper" markdown>

## Research Highlights
<div class="swiper-wrapper" markdown>

{% for paper in research_highlights %}
<div class="swiper-slide" markdown>

<a href="{{ paper.link }}" target=_blank>
<div class="card" markdown>
<center>
<img src="./assets/teasers/{{ paper.key }}-teaser.png" markdown>
<b>{{ paper.title }} ({{ paper.venue }})</b><br>
{{ paper.desc }}<br>
</center>
</div>
</a>

</div>
{% endfor %}

</div>
<div class="swiper-pagination"></div>
</div>


<div class="container" markdown>

<!-- News -->
<div class="news" markdown>
## News
{% for item in news %}
{% if loop.index <= 3 %}
- __[{{ item.time }}]__ {% if item.link %}<a href="{{ item.link }}" target="_blank">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}
{% endif %}
{% endfor %}

[__View all__](news.md)
</div>

<!-- 3D Gallery -->
<div class="gallery" markdown>
## 3D Gallery

<iframe width="100%" height="240em" src="./assets/gallery/nupzuki1.html" frameborder="0" scrolling="no"></iframe>

</div>

</div>



<!-- Swiper JS -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Initialize Swiper -->
<script>
var swiper = new Swiper(".research-highlights-swiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});
</script>

