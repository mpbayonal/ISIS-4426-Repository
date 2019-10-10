import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VerDisenoComponent } from './ver-diseno.component';

describe('VerDisenoComponent', () => {
  let component: VerDisenoComponent;
  let fixture: ComponentFixture<VerDisenoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VerDisenoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VerDisenoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
