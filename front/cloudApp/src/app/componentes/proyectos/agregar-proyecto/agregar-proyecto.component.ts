import { Component, OnInit } from '@angular/core';
import { ProyectoService } from 'src/app/servicios/proyecto/proyecto.service';
import {Router} from '@angular/router'


@Component({
  selector: 'app-agregar-proyecto',
  templateUrl: './agregar-proyecto.component.html',
  styleUrls: ['./agregar-proyecto.component.css']
})
export class AgregarProyectoComponent implements OnInit {

  constructor(private proyectoService: ProyectoService, private router: Router) { }

  proyecto = {
    nombre: '',
    descripcion: '',
    pago: '',
    empresa: localStorage.getItem("id")
  }
  agregarProyecto(){
    this.proyectoService.agregarProyecto(this.proyecto).subscribe(
      res=>{
        this.router.navigate( ['empresa/'+localStorage.getItem("url") +'/proyectos']);
      },
      err=> console.log(err)
    );  

    
  }
  ngOnInit() {
    
  }

}
