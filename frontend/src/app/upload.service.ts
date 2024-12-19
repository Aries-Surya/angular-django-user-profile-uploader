import { Injectable } from '@angular/core';
import { HttpClient, HttpEventType, HttpRequest } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  private baseUrl = 'http://localhost:8000/api/upload/';

  constructor(private http: HttpClient) {}

  upload(file: File): Observable<any> {
    const formData: FormData = new FormData();
    formData.append('file', file);

    const req = new HttpRequest('POST', this.baseUrl, formData, {
      reportProgress: true,
      responseType: 'json'
    });

    return this.http.request(req).pipe(
      map(event => {
        switch (event.type) {
          case HttpEventType.UploadProgress:
            const progress = event.total ? Math.round(100 * event.loaded / event.total) : 0;
            console.log(`Upload progress: ${progress}%`);
            return { status: 'progress', message: progress };
          case HttpEventType.Response:
            console.log('Upload response:', event.body);
            return { status: 'success', body: event.body };
          default:
            console.log('Unhandled event:', event);
            return { status: 'unknown', event };
        }
      })
    );
  }
}
