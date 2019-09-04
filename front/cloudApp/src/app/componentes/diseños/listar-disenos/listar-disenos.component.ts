import { Component, OnInit } from '@angular/core';
import { DiseñoService } from 'src/app/servicios/diseño/diseño.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-listar-disenos',
  templateUrl: './listar-disenos.component.html',
  styleUrls: ['./listar-disenos.component.css']
})
export class ListarDisenosComponent implements OnInit {

  disenos: any = [];
 
 
  constructor(private diseñosService: DiseñoService,private rutaActiva: ActivatedRoute, private router: Router ) { }

  
  ngOnInit() {
    this.diseñosService.getDisenos(this.rutaActiva.snapshot.params.idProyecto).subscribe(
      res=>{
        this.disenos=res;
      }, err => console.log(err)
    )
  }

  formularioAgregarDiseno(){
    this.router.navigate(["empresa/proyectos/"+ this.rutaActiva.snapshot.params.idProyecto +"/disenos/agregarDiseno"])
  }
  detalleDisenos(id){
    this.router.navigate(["empresa/proyectos/diseños/"+id])
  }
}
