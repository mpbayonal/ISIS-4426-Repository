import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';

const API_URI = environment.backend_url;

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http: HttpClient, private router: Router) { }

  getUrl(username) {
    return this.http.get(`${API_URI}/user/${username}/`);
  }

  loginUsuario(usuario) {
    return this.http.post(`${API_URI}/auth/login/`, usuario);
  }

  signUpUsuario(usuario) {
    return this.http.post(`${API_URI}/auth/signup/`, usuario);
  }

  setToken(token): void {
    localStorage.setItem('accessToken', token);
  }

  getToken() {
    return localStorage.getItem('accessToken');
  }
  logoutUser() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('usuario');
    localStorage.removeItem('url');
    localStorage.removeItem('id');
    this.router.navigate(['/']);
  }
}
