---
hide:
  - navigation
  - toc
---

<style>
p { text-align: justify; }

.container {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-gap: 1rem;
}

.swiper {
    width: 100%;
    height: 100%;
}

.swiper-slide {
    margin-bottom: 1em;
}

.news-section {
    justify-items: center;
    align-items: center;
}

@media only screen and (max-width: 600px) {
    .container {
        grid-template-columns: 1fr;
    }
}
</style>


# KAIST Geometric AI Group
KAIST Geometric AI Lab led by Prof. Minhyuk Sung focuses on developing novel machine learning techniques to solve fundamental problems in 3D geometric data processing and analysis. The 3D data, arising both from sensing the real world as well as in creating content by designers, are widely used in numerous applications in computer vision, computer graphics, and robotics. 3D data is distinguished from the other data modalities by its unique characteristics, such as sparsity, irregularity, fidelity (representing 3D objects as they present in the real world), and their roles as domains wherein the other information is defined (such as physical attributes and semantic annotations). Such characteristics introduce challenging research problems, which cannot be directly solved with conventional techniques developed to process regularly sampled signal data like audio and images. Our goal is to develop novel methodologies specialized in 3D based upon a profound understanding of its nature.

<!-- Link Swiper's CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

<div class="container" markdown>


<!-- Researh Highlights -->
<div class="swiper research-highlights-swiper" markdown>

## Researh Highlights
<div class="swiper-wrapper" markdown>


<div class="swiper-slide" markdown>
<div class="card" markdown>
<center markdown>
<img src="./assets/teasers/salad-teaser.png" markdown>
<b>SALAD: Part-Level Latent Diffusion for 3D Shape Generation and Manipulation<br>(ICCV 2023)</b><br>
A cascaded diffusion model based on a part-level implicit 3D representation.<br>
</center>
</div>
</div>

<div class="swiper-slide" markdown>
<div class="card" markdown>
<center markdown>
<img src="./assets/teasers/syncdiffusion-teaser.png" markdown>
<b> SyncDiffusion: Coherent Montage via Synchronized Joint Diffusions (NeurIPS 2023)</b><br>
A plug-and-play module that synchronizes multiple reverse diffusion processes, producing coherent images of various sizes without additional training.<br>
</center>
</div>
</div>


</div>
<div class="swiper-pagination"></div>
</div>


<!-- News -->
<div class="news-section" markdown>
## News
- __[Jan 2024]__ One paper has been accepted to 3DV 2024.
- __[Sep 2023]__ Two papers accepted to NeurIPS 2023.
- __[Jul 2023]__ One paper has been accepted to Pacific Graphics 2023.

__View all__
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
        delay: 4000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});
</script>

