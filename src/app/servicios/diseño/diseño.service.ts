import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

const API_URI = environment.backend_url;

@Injectable({
  providedIn: 'root'
})
export class DiseñoService {

  constructor(private http: HttpClient) { }

  getDisenos(proyecto) {
    return this.http.get(`${API_URI}/disenos/${proyecto}`);
  }
  createDiseno(diseno) {
    return this.http.post(`${API_URI}/diseno/`, diseno);
  }
  getDisenoId(id) {
    return this.http.get(`${API_URI}/diseno/${id}`);
  }

}
