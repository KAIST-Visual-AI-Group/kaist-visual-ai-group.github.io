---
hide:
  - navigation
  - toc
---

<style>
p { text-align: justify; }

.md-typeset h1 { margin: 0; }

.md-typeset .grid {
  grid-template-columns: repeat(auto-fit, minmax(90%, 1fr))
}

.research-highlights-section {
    display: inline-table;
    width: 66% !important;
    padding: 0 10px 0 0;
    vertical-align: top;
    p { margin: 0px; }
}

.news-section {
    display: inline-table;
    width: 33% !important;
    padding: 0 0 0 10px;
    vertical-align: top;
    p { margin: 0px; }
}

.research-highlight-thumbnail {
    width: 80px;
    width: calc(70% - 12px) !important;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media only screen and (max-width: 600px) {
    .research-highlights-section {
        width: 100% !important;
    }

    .news-section {
        width: 100% !important;
    }
}
</style>


# KAIST Geometric AI Group
KAIST Geometric AI Lab led by Prof. Minhyuk Sung focuses on developing novel machine learning techniques to solve fundamental problems in 3D geometric data processing and analysis. The 3D data, arising both from sensing the real world as well as in creating content by designers, are widely used in numerous applications in computer vision, computer graphics, and robotics. 3D data is distinguished from the other data modalities by its unique characteristics, such as sparsity, irregularity, fidelity (representing 3D objects as they present in the real world), and their roles as domains wherein the other information is defined (such as physical attributes and semantic annotations). Such characteristics introduce challenging research problems, which cannot be directly solved with conventional techniques developed to process regularly sampled signal data like audio and images. Our goal is to develop novel methodologies specialized in 3D based upon a profound understanding of its nature.

<!-- Link Swiper's CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
<br>


<!-- Swiper -->
<div class="swiper research-highlights-swiper">
<div class="swiper-wrapper">

<div class="swiper-slide">
<div class="card" markdown>
<img src="./assets/teasers/syncdiffusion-teaser.png" markdown>
<b> SyncDiffusion: Coherent Montage via Synchronized Joint Diffusions </b><br>
A plug-and-play module that synchronizes multiple reverse diffusion processes, producing coherent images of various sizes without additional training.
<p></p><br>
</div>
</div>

<div class="swiper-slide">
<div class="card" markdown>
<img src="./assets/teasers/salad-teaser.png" markdown>
<b> SALAD: Part-Level Latent Diffusion for 3D Shape Generation and Manipulation </b><br>
A cascaded diffusion model based on a part-level implicit 3D representation.
<br><br>
</div>
</div>

</div>
<div class="swiper-pagination"></div>
</div>


<!-- Swiper JS -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Initialize Swiper -->
<script>
var swiper = new Swiper(".research-highlights-swiper", {
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});
</script>

