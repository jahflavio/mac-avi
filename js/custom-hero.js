window.addEventListener("load", () => {
  if (typeof gsap === "undefined" || typeof ScrollTrigger === "undefined") {
    console.error("GSAP or ScrollTrigger is not loaded.");
    return;
  }

  // Refresca TODOS los triggers de la página después de que todo ha cargado.
  ScrollTrigger.refresh();

  // Animación para la sección Hero
  const heroSection = document.querySelector("#inicio");
  const heroBadge = document.querySelector("#hero-badge");
  const heroTitle = document.querySelector("#hero-title");
  const heroText = document.querySelector("#hero-text");
  const heroButton = document.querySelector("#hero-button");
  const heroOverlay = document.querySelector("#hero-gradient-overlay");

  if (heroSection && heroBadge && heroTitle && heroText && heroButton && heroOverlay) {
    gsap.set([heroBadge, heroTitle, heroText, heroButton], { opacity: 0, y: 30 });
    gsap.set(heroOverlay, { opacity: 0 });
    
    const tlHero = gsap.timeline({
      scrollTrigger: {
        trigger: heroSection,
        start: "top top",
        end: "center center",
        scrub: 1,
      },
    });

    tlHero.to(heroOverlay, { opacity: 1, ease: "none" }, 0)
          .to(heroBadge, { opacity: 1, y: 0, ease: "power2.out", delay: 0.5 }, 0)
          .to(heroTitle, { opacity: 1, y: 0, ease: "power2.out", delay: 0.7 }, 0)
          .to(heroText, { opacity: 1, y: 0, ease: "power2.out", delay: 0.9 }, 0)
          .to(heroButton, { opacity: 1, y: 0, ease: "power2.out", delay: 1.1 }, 0);
  }

  // Animación para la sección Nosotros
  const nosotrosSection = document.querySelector("#nosotros");
  if (nosotrosSection) {
    const nosotrosElements = nosotrosSection.querySelectorAll(".rv-badge, h2, h5, p, ul");

    // Asegurarse de que los elementos estén ocultos al inicio de esta animación
    gsap.set(nosotrosElements, { opacity: 0, y: 50 });

    const tlNosotros = gsap.timeline({
      scrollTrigger: {
        trigger: nosotrosSection,
        start: "top 60%", // Inicia cuando la parte superior de la sección está al 60% del viewport
        // end: "bottom 20%", // Opcional: define cuándo termina la animación
        toggleActions: "play none none none", // Reproducir una vez y no revertir
        // markers: true, // Para depuración
      },
    });

    tlNosotros.to(nosotrosElements, {
      opacity: 1,
      y: 0,
      stagger: 0.1, // Animación escalonada para los elementos
      ease: "power2.out",
      duration: 1
    });
  }

});