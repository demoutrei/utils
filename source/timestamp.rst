:description: Datetime to timestamp converter


Timestamp Converter
===================


.. jupyter-execute::
    :hide-code:

    from datetime import datetime
    import panel

    panel.extension()
    dark_picker_css = """
    :host {
      background-color: #1a1a1a !important;
      color: #ffffff !important;
    }

    input {
      background-color: #262626 !important;
      color: #ffffff !important;
      border: 1px solid #404040 !important;
      font-family: "Twemoji Country Flags", var(--sy-f-text);
    }
    
    .flatpickr-calendar, .flatpickr-month, .flatpickr-current-month, .flatpickr-monthDropdown-months, .flatpickr-weekdays, .dayContainer, .flatpickr-day, .flatpickr-time-separator, .flatpickr-weekday {
      background-color: #1a1a1a !important;
      box-shadow: none !important;
      color: white !important;
      font-family: "Twemoji Country Flags", var(--sy-f-text);
    }

    .flatpickr-day.prevMonthDay, .flatpickr-day.nextMonthDay {
      color: #484848 !important;
      font-family: "Twemoji Country Flags", var(--sy-f-text);
    }

    .flatpickr-day.selected, .flatpickr-day.selected:hover {
      border-color: var(--accent-9);
      font-family: "Twemoji Country Flags", var(--sy-f-text);
    }
    
    .flatpickr-day:hover, .flatpickr-month:hover {
      background-color: #404040 !important;
      font-family: "Twemoji Country Flags", var(--sy-f-text);
    }

    .flatpickr-days, .flatpickr-time {
      border: none !important;
      font-family: "Twemoji Country Flags", var(--sy-f-text);
    }
    """
    picker = panel.widgets.DatetimePicker(
      stylesheets = [dark_picker_css],
      value = datetime.now(),
      allow_input = True,
      disabled = False,
      css_classes = ["datetime-picker"]
    )

    picker


.. jupyter-execute::
    :hide-code:

    int(picker.value.timestamp())