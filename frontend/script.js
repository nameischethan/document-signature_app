console.log("script loaded");

const BASE_URL = "https://document-signature-app-n6y9.onrender.com/api";

// Upload Document
async function uploadDocument() {

    const fileInput = document.getElementById("pdfFile");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a PDF file");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

        const response = await fetch(
            `${BASE_URL}/document/upload`,
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        document.getElementById("documentResult").innerText =
            `Document Uploaded Successfully. ID: ${data.id}`;

        console.log(data);

    } catch (error) {

        console.error(error);
        alert("Upload failed");
    }
}


// Upload Signature
async function uploadSignature() {

    const fileInput =
        document.getElementById("signatureFile");

    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a signature image");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

        const response = await fetch(
            `${BASE_URL}/signature/upload`,
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        document.getElementById("signatureResult").innerText =
            `Signature Uploaded Successfully. ID: ${data.id}`;

        console.log(data);

    } catch (error) {

        console.error(error);
        alert("Upload failed");
    }
}


// Sign Document
async function signDocument() {

    const documentId =
        document.getElementById("documentId").value;

    const signatureId =
        document.getElementById("signatureId").value;

    if (!documentId || !signatureId) {
        alert("Enter Document ID and Signature ID");
        return;
    }

    try {

        const response = await fetch(
            `${BASE_URL}/document/sign?document_id=${documentId}&signature_id=${signatureId}`,
            {
                method: "POST"
            }
        );

        const data = await response.json();

        document.getElementById("signResult").innerHTML = `
            <p style="color:green;">
                ${data.message}
            </p>

            <a href="http://127.0.0.1:8000/${data.signed_file}"
               target="_blank">
               📄 Download Signed PDF
            </a>
        `;

        console.log(data);

    } catch (error) {

        console.error(error);
        alert("Signing failed");
    }
}