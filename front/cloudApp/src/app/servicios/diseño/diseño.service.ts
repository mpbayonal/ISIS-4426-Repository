import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DiseñoService {

  API_URI = 'http://172.24.42.47:8080';
  constructor(private http: HttpClient) { }

  getDisenos(proyecto){
    return this.http.get(`${this.API_URI}/disenos/${proyecto}`);
  }
  createDiseno(diseno){
    return this.http.post(`${this.API_URI}/diseno/`, diseno)
  }
  getDisenoId(id){
    return this.http.get(`${this.API_URI}/diseno/${id}`);
  }
  
}
