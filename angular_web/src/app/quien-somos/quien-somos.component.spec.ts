import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QuienSomosComponent } from './quien-somos.component';

describe('QuienSomosComponent', () => {
  let component: QuienSomosComponent;
  let fixture: ComponentFixture<QuienSomosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QuienSomosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QuienSomosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
