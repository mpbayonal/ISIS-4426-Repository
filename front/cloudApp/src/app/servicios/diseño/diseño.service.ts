import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DiseñoService {

  API_URI = 'http://localhost:8000/';
  constructor(private http: HttpClient) { }

  
}
