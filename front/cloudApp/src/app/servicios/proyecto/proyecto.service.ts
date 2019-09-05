import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ProyectoService {

  API_URI = 'http://172.24.42.47:8080';
  constructor(private http: HttpClient) { }


  getProyectos(empresa: string){
    return this.http.get(`${this.API_URI}/proyecto/${empresa}`);
  }
  agregarProyecto(proyecto){
    return this.http.post(`${this.API_URI}/proyectos/`, proyecto);
  }
  editarProyecto(proyecto, idProyecto){
    return this.http.put(`${this.API_URI}/proyectos/${idProyecto}/`, proyecto);
  }
  eliminarProyecto(idProyecto){
    return this.http.delete(`${this.API_URI}/proyectos/${idProyecto}`);
  }
}
