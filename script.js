
// ==========================================
// API URL
// ==========================================
const API_URL = "https://credit-card-scdt.onrender.com";


// ==========================================
// GET HTML ELEMENTS
// ==========================================

const features =
    document.getElementById("features");

const form =
    document.getElementById("transactionForm");

const resultBox =
    document.getElementById("result");

const resultText =
    document.getElementById("resultText");

const resultMessage =
    document.getElementById("resultMessage");

const resultIcon =
    document.getElementById("resultIcon");

const analyzeButton =
    document.getElementById("analyzeButton");


// ==========================================
// CREATE V1 - V28 INPUTS
// ==========================================

for (let i = 1; i <= 28; i++) {

    features.innerHTML += `

        <div class="feature">

            <label for="V${i}">
                V${i}
            </label>

            <input
                type="number"
                id="V${i}"
                step="any"
                value="0"
                required
            >

        </div>

    `;
}


// ==========================================
// ADVANCED FEATURES TOGGLE
// ==========================================

const toggleButton =
    document.getElementById("toggleFeatures");

const toggleIcon =
    document.getElementById("toggleIcon");

const featureSection =
    document.getElementById("featureSection");


toggleButton.addEventListener(
    "click",
    function () {

        if (
            featureSection.style.display ===
            "block"
        ) {

            featureSection.style.display =
                "none";

            toggleIcon.innerText = "+";

        } else {

            featureSection.style.display =
                "block";

            toggleIcon.innerText = "−";

        }

    }
);


// ==========================================
// FORM SUBMISSION
// ==========================================

form.addEventListener(
    "submit",
    async function (event) {

        // Stop page refresh
        event.preventDefault();


        // ==================================
        // GET MAIN VALUES
        // ==================================

        let data = {

            Time: Number(
                document.getElementById(
                    "Time"
                ).value
            ),

            Amount: Number(
                document.getElementById(
                    "Amount"
                ).value
            )

        };


        // ==================================
        // GET V1 - V28
        // ==================================

        for (let i = 1; i <= 28; i++) {

            data["V" + i] =
                Number(
                    document.getElementById(
                        "V" + i
                    ).value
                );

        }


        // ==================================
        // BUTTON LOADING
        // ==================================

        analyzeButton.disabled = true;

        analyzeButton.innerText =
            "ANALYZING...";


        // ==================================
        // SEND DATA TO FASTAPI
        // ==================================

        try {

            const response =
                await fetch(
                    `${API_URL}/predict`,
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(data)

                    }
                );


            // ==================================
            // CHECK SERVER RESPONSE
            // ==================================

            if (!response.ok) {

                throw new Error(
                    "Server returned an error"
                );

            }


            const result =
                await response.json();


            // ==================================
            // SHOW RESULT
            // ==================================

            resultBox.classList.remove(
                "hidden"
            );


            // ==================================
            // FRAUD
            // ==================================

            if (result.prediction === 1) {

                resultText.innerText =
                    "Fraudulent Transaction";

                resultMessage.innerText =
                    result.message;

                resultIcon.innerText =
                    "!";


                resultBox.style.background =
                    "#fef2f2";

                resultBox.style.borderColor =
                    "#fecaca";

                resultIcon.style.background =
                    "#dc2626";

            }


            // ==================================
            // GENUINE
            // ==================================

            else {

                resultText.innerText =
                    "Genuine Transaction";

                resultMessage.innerText =
                    result.message;

                resultIcon.innerText =
                    "✓";


                resultBox.style.background =
                    "#f0fdf4";

                resultBox.style.borderColor =
                    "#bbf7d0";

                resultIcon.style.background =
                    "#16a34a";

            }

        }


        // ==================================
        // CONNECTION ERROR
        // ==================================

        catch (error) {

            resultBox.classList.remove(
                "hidden"
            );

            resultText.innerText =
                "Connection Error";

            resultMessage.innerText =
                "Unable to connect to the fraud detection server. Make sure FastAPI is running.";

            resultIcon.innerText =
                "!";


            resultBox.style.background =
                "#fef2f2";

            resultBox.style.borderColor =
                "#fecaca";

            resultIcon.style.background =
                "#dc2626";

        }


        // ==================================
        // RESTORE BUTTON
        // ==================================

        analyzeButton.disabled = false;

        analyzeButton.innerText =
            "ANALYZE TRANSACTION";

    }
);

