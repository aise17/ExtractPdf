import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IrOcrComponent } from './ir-ocr.component';

describe('IrOcrComponent', () => {
  let component: IrOcrComponent;
  let fixture: ComponentFixture<IrOcrComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IrOcrComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IrOcrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
