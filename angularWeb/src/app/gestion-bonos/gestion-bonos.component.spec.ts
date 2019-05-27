import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GestionBonosComponent } from './gestion-bonos.component';

describe('GestionBonosComponent', () => {
  let component: GestionBonosComponent;
  let fixture: ComponentFixture<GestionBonosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GestionBonosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GestionBonosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
