import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ProyectoService {

  API_URI = 'http://localhost:8000';
  constructor(private http: HttpClient) { }


  getProyectos(empresa: string){
    return this.http.get(`${this.API_URI}/proyecto/${empresa}`);
  }
  agregarProyecto(proyecto, empresa){
    return this.http.post(`${this.API_URI}/proyectos/${empresa}/crear/`, proyecto);
  }
  editarProyecto(proyecto, idProyecto){
    return this.http.put(`${this.API_URI}/proyectos/${idProyecto}/`, proyecto);
  }
  eliminarProyecto(idProyecto){
    return this.http.delete(`${this.API_URI}/proyectos/${idProyecto}`);
  }
  getProyecto(id){
    return this.http.get(`${this.API_URI}/proyectos/${id}/`)
  }
}
