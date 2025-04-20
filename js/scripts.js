function exportPDF() {
  // Dynamically load html2pdf.js if not present
  if (!window.html2pdf) {
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
    script.onload = generatePDF;
    document.body.appendChild(script);
  } else {
    generatePDF();
  }
}

function generatePDF() {
  // Select only printable sections
  const elements = document.querySelectorAll('.printable');
  const wrapper = document.createElement('div');
  wrapper.classList.add('force-dark-mode');
  elements.forEach(el => wrapper.appendChild(el.cloneNode(true)));

  var opt = {
    margin:       0.5,
    filename:     'QuantumHealingGuide.pdf',
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2, backgroundColor: '#0d1e13' },
    jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' },
    pagebreak:    { mode: ['avoid-all', 'css', 'legacy'] }
  };
  html2pdf().set(opt).from(wrapper).save();
}
