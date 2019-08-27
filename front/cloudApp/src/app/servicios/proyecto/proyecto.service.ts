import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProyectoService {

  API_URI = 'http://localhost:8000/';
  constructor(private http: HttpClient) { }


  getProyectos(){
    return this.http.get(`${this.API_URI}getdata`)
  }
}
