import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpRequest } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

const API_URI = environment.backend_url;

@Injectable({
  providedIn: 'root'
})
export class DiseñoService {

  constructor(private http: HttpClient) { }

  getDisenos(proyecto): Observable<any>  {
    return this.http.get(`${API_URI}/disenos/${proyecto}/`);
  }
  createDiseno(diseno): Observable<any>  {
    return this.http.post(`${API_URI}/diseno/`, diseno);
  }
  getDisenoId(id): Observable<any>  {
    return this.http.get(`${API_URI}/diseno/${id}/`);
  }
  getUploadUrl(data): Observable<any> {
    return this.http.post(`${API_URI}/uploadkey/`, data);
  }

  uploadfileAWSS3(fileuploadurl: string, contenttype: string, file: any): Observable<any> {
    // this will be used to upload all csv files to AWS S3
    const headers = new HttpHeaders({ 'Content-Type': contenttype });
    const options = {
      headers,
      reportProgress: false, // This is required for track upload process
    };
    const req = new HttpRequest('PUT', fileuploadurl, file, options);
    return this.http.request(req);
  }

}
