const encodeSection = document.querySelector("#encode-section");
const decodeSection = document.querySelector("#decode-section");
const sectionTitle = document.querySelector(".container > h1");
const guideMessage = document.querySelector("#guide-message");
const textInput = document.querySelector("#text-input");
const demoMode = document.querySelector("#demo_mode");
const encodedImage = document.querySelector(".img-display");
const decodedText = document.querySelector("#decoded-text");
const encodedImg = document.querySelector(".img-display > img");

encodeSection.addEventListener("click", () => {
    sectionTitle.textContent = "Encode Demo";
    guideMessage.textContent = "Choose an image and a message to encode";
    textInput.classList.remove("hidden");
    demoMode.setAttribute("value", "encode");
    encodedImage.classList.remove("hidden");
    decodedText.classList.add("hidden");
});

decodeSection.addEventListener("click", () => {
    sectionTitle.textContent = "Decode Demo";
    guideMessage.textContent = "Choose an image to decode";
    textInput.classList.add("hidden");
    demoMode.setAttribute("value", "decode");
    encodedImage.classList.add("hidden");
    decodedText.classList.remove("hidden");
});

$("#encode-form").submit(function(e) {            
    e.preventDefault();

    var csrfmiddlewaretoken = $("#encode-form").find("input[name='csrfmiddlewaretoken']" ).val();
    
    var data = new FormData($('form').get(0));            
    $.ajax({
        method: "POST",                
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        MimeType: "multipart/form-data",
        success: (data) => {
            document.write(data);
        }
    });
});


$("#encode-form").submit(function(e) {            
    e.preventDefault();

    var csrfmiddlewaretoken = $("#encode-form").find("input[name='csrfmiddlewaretoken']" ).val();
    
    var data = new FormData($('form').get(0));            
    $.ajax({
        method: "POST",                
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        MimeType: "multipart/form-data",
        success: (data) => {
            // console.log(data);
            // document.body.innerHTML = '';
            // document.write(data)
            decodedMessage.textContent = data;
        }
    });
});