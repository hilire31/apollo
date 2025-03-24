import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PdfService {
  private apiUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  uploadPdf(file: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', file);
    console.log("bbb");
    return this.http.post(`${this.apiUrl}/upload/`, formData);
  }

  processText(text: string): Observable<any> {
    console.log(text);
    return this.http.post(`${this.apiUrl}/process/`, { text });
  }
}
