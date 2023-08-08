function openPreview(x) {
    const container = document.getElementById("preview-container");

    var previewImage = new Image();
    previewImage.src = x.src;

    container.style.display = "flex";
    var screenHeight = window.innerHeight;
    var screenWidth = window.innerWidth;
    var containerHeight1 = container.offsetHeight;
    var containerWidth1 = container.offsetWidth;



    function addImage() {
    const containerWidth = container.width;
    const containerHeight = container.height;
    const imageAspectRatio = previewImage.width / previewImage.height;
    const containerAspectRatio = containerWidth / containerHeight;

    if (imageAspectRatio > containerAspectRatio) {
        previewImage.width = containerWidth * 0.5; // set the width to the maximum value
        previewImage.height = previewImage.width / imageAspectRatio; // calculate the height based on the aspect ratio
    } else {
        previewImage.height = containerHeight * 0.5; // set the height to the maximum value
        previewImage.width = previewImage.height * imageAspectRatio; // calculate the width based on the aspect ratio
    }

    container.style.top = (screenHeight - containerHeight1) /2 + "px";
    container.style.left = (screenWidth - containerWidth1) /2 + "px";
    container.appendChild(previewImage);
    }


    if (document.readyState === 'complete') {
        addImage();
    } else {
        window.onload = addImage();
    }
    
    function closePreview() {
        container.removeEventListener("click", closePreview);
        container.removeChild(container.lastChild);
        container.style.display = "none";
    }

    container.addEventListener("click", closePreview);
}
