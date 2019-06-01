import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RequestByYearEstadisticaAdminComponent } from './request-by-year-estadistica-admin.component';

describe('RequestByYearEstadisticaAdminComponent', () => {
  let component: RequestByYearEstadisticaAdminComponent;
  let fixture: ComponentFixture<RequestByYearEstadisticaAdminComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RequestByYearEstadisticaAdminComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RequestByYearEstadisticaAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
