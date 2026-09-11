document.addEventListener(
  "DOMContentLoaded",
  function(_) {
    setTimeout(() => {
      const bokehViews = Bokeh.index;
      const t1 = document.querySelector('.output span[data-line="1"]');
      for (let key in bokehViews) {
        const view = bokehViews[key];
        if (view.model && view.model.css_classes && view.model.css_classes.includes("datetime-picker")) {
          view.model.connect(view.model.properties.value.change, () => {
            let timestamp = view.model.value;
            let date = new Date(timestamp);
            t1.textContent = date.getTime();
          });
        }
      }
    }, 1000);
  }
);