// noSolutions/my-angular-django-app/frontend/src/app/upload/upload.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UploadService } from '../upload.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css'],
  standalone: true,
  imports: [CommonModule]
})
export class UploadComponent {
  selectedFile: File | null = null;
  progress: number = 0;
  message: string = '';

  constructor(private uploadService: UploadService) {}

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
      console.log('File selected:', this.selectedFile.name);
    }
  }

  onUpload(): void {
    if (this.selectedFile) {
      console.log('Starting upload...');
      this.uploadService.upload(this.selectedFile).subscribe({
        next: (event: any) => {
          if (event.status === 'progress') {
            this.progress = event.message;
            console.log(`Upload progress: ${this.progress}%`);
          } else if (event.status === 'success') {
            this.message = 'Upload successful!';
            console.log('Upload successful:', event.body);
          }
        },
        error: (err: any) => {
          console.error('Upload error:', err);
          this.message = 'Upload failed!';
        },
        complete: () => {
          console.log('Upload complete');
        }
      });
    }
  }
}