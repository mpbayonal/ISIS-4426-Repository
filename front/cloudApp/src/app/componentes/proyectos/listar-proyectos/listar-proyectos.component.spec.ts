import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarProyectosComponent } from './listar-proyectos.component';

describe('ListarProyectosComponent', () => {
  let component: ListarProyectosComponent;
  let fixture: ComponentFixture<ListarProyectosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListarProyectosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarProyectosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
