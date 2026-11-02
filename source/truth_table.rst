Truth Table
===========

.. raw:: html

    <div id="div-inputContainer" style="display: flex; justify-content: space-between;">
    <input id="input-expression" type="text" placeholder="Enter propositional logic expression..." style="width: 85%; border: 1px solid white; border-radius: 7px; padding: 3px 7px;"/>
    <button id="button-submit" onclick="calculate();" style="border: 1px solid white; border-radius: 10px; padding: 6px;">Submit</button>
    </div>
    <div class="table-wrapper docutils container">
      <table id="truthTable" class="docutils align-default">
        <thead>
          <tr class="row-odd">
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    </div>
    <script>
      async function calculate() {
        const expression = document.querySelector("#input-expression").value;
        if (expression.trim() === "") return;
        document.querySelector("#truthTable").querySelector("thead").querySelector("tr.row-odd").replaceChildren();
        document.querySelector("#truthTable").querySelector("tbody").replaceChildren();
        const response = await fetch("https://api.demoutrei.dev/math/truth_table", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            "expression": expression
          })
        });
        if (!response.ok) return;
        const data = await response.json();
        for (const key of Object.keys(data)) {
          const header = document.createElement("th");
          header.className = "head";
          const content = document.createElement("p");
          content.textContent = key;
          header.appendChild(content);
          document.querySelector("#truthTable").querySelector("thead").querySelector("tr.row-odd").appendChild(header);
        }
        const rowLength = data[Object.keys(data)[0]].length;
        for (let i = 0; i < rowLength; i += 1) {
          const rowElement = document.createElement("tr");
          rowElement.className = i % 2 == 0 ? "row-even" : "row-odd";
          document.querySelector("#truthTable").querySelector("tbody").appendChild(rowElement);
          for (const [index, key] of Object.keys(data).entries()) {
            const dataElement = document.createElement("td");
            const contentElement = document.createElement("p");
            const value = data[key][i];
            const valueElement = document.createElement("span");
            valueElement.textContent = value == 1 ? "True" : "False";
            const badgeStyle = value == 1 ? "success" : "danger";
            valueElement.classList.add("sd-sphinx-override", "sd-badge", `sd-outline-${badgeStyle}`, `sd-text-${badgeStyle}`);
            contentElement.appendChild(valueElement);
            dataElement.appendChild(contentElement);
            document.querySelector("#truthTable").querySelector("tbody").querySelectorAll("tr")[i].appendChild(dataElement);
          }
        }
      }
    </script>