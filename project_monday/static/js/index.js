document.addEventListener("htmx:beforeSwap", (e) => {

      const target = event.detail.target;
      
      target.classList.remove("slide-in");
      
      void target.offsetWidth;

      target.classList.add("slide-in"); 
});
