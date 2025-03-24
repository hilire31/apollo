import { Component } from '@angular/core';
import { PdfService } from './pdf.service';

@Component({
  selector: 'app-pdf',
  templateUrl: './pdf.component.html'
})
export class PdfComponent {
  uploadedText: string = '';
  processedText: string = '';

  constructor(private pdfService: PdfService) {}

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.pdfService.uploadPdf(file).subscribe((response) => {
        this.uploadedText = response.text;
      });
    }
  }

  onProcessText() {
    this.pdfService.processText(this.uploadedText).subscribe((response) => {
      this.processedText = response.processed_text;
    });
  }
}
