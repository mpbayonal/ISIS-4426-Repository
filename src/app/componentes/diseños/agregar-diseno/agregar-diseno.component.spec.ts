import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AgregarDisenoComponent } from './agregar-diseno.component';

describe('AgregarDisenoComponent', () => {
  let component: AgregarDisenoComponent;
  let fixture: ComponentFixture<AgregarDisenoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AgregarDisenoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AgregarDisenoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
