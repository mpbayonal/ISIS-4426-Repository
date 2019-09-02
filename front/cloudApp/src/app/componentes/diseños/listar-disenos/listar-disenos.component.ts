import { Component, OnInit } from '@angular/core';
import { DiseñoService } from 'src/app/servicios/diseño/diseño.service';

@Component({
  selector: 'app-listar-disenos',
  templateUrl: './listar-disenos.component.html',
  styleUrls: ['./listar-disenos.component.css']
})
export class ListarDisenosComponent implements OnInit {

  diseños: any = [];
  constructor(private diseñosService: DiseñoService) { }

  ngOnInit() {
    
  }

}
