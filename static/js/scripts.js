// let form1 = document.querySelector('.form1');
// let form2 = document.querySelector('.form2');
// let form3 = document.querySelector('.form3');
// let click1 = document.querySelector('.click1');
// let click2 = document.querySelector('.click2');
// let click3 = document.querySelector('.click3');

// click1.addEventListener('click', (e) => {
//     form3.classList.add("hidden");
//     form2.classList.add("hidden");
//     form1.classList.remove("hidden");
//     e.preventDefault();
// })
// click2.addEventListener('click', (e) => {
//     form3.classList.add("hidden");
//     form1.classList.add("hidden");
//     form2.classList.remove("hidden");
//     e.preventDefault();
// })
// click3.addEventListener('click', (e) => {
//     form2.classList.add("hidden");
//     form1.classList.add("hidden");
//     form3.classList.remove("hidden");
//     e.preventDefault();
// })

// // add an event listener for the official time tab to hide the overload tabs when clicked
// let officialTimeTab = document.querySelector('#official-time-tab');
// officialTimeTab.addEventListener('click', (e) => {
//     form2.classList.add("hidden");
//     form3.classList.add("hidden");
//     form1.classList.remove("hidden");
//     e.preventDefault();
// })

// click1.click();

import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

function generatePDF() {
  // Use html2canvas to capture the HTML content as an image
  html2canvas(document.getElementById("content")).then(function(canvas) {
    // Use jsPDF to create a PDF document and add the captured image as a page
    var pdf = new jsPDF();
    pdf.addImage(canvas.toDataURL("image/png"), "PNG", 0, 0, pdf.internal.pageSize.getWidth(), 0, null, false);
    pdf.save("download.pdf");
  });
}
