import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

const API_URI = environment.backend_url;

@Injectable({
  providedIn: 'root'
})
export class ProyectoService {

  constructor(private http: HttpClient) { }


  getProyectos(empresa: string) {
    return this.http.get(`${API_URI}/proyecto/${empresa}/`);
  }
  agregarProyecto(proyecto, empresa) {
    return this.http.post(`${API_URI}/proyectos/${empresa}/crear/`, proyecto);
  }
  editarProyecto(proyecto, idProyecto) {
    return this.http.put(`${API_URI}/proyectos/${idProyecto}/`, proyecto);
  }
  eliminarProyecto(idProyecto) {
    return this.http.delete(`${API_URI}/proyectos/${idProyecto}`);
  }
  getProyecto(id) {
    return this.http.get(`${API_URI}/proyectos/${id}/`);
  }
}
