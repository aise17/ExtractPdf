import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CompraBonosEstadisticaAdminComponent } from './compra-bonos-estadistica-admin.component';

describe('CompraBonosEstadisticaAdminComponent', () => {
  let component: CompraBonosEstadisticaAdminComponent;
  let fixture: ComponentFixture<CompraBonosEstadisticaAdminComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CompraBonosEstadisticaAdminComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CompraBonosEstadisticaAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
