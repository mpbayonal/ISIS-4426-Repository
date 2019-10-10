import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AgregarProyectoComponent } from './agregar-proyecto.component';

describe('AgregarProyectoComponent', () => {
  let component: AgregarProyectoComponent;
  let fixture: ComponentFixture<AgregarProyectoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AgregarProyectoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AgregarProyectoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
