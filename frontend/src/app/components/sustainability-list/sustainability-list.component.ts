import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SustainabilityService } from '../../services/sustainability.service';
import { SustainabilityAction } from '../../models/sustainability-action';

@Component({
  selector: 'app-sustainability-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './sustainability-list.component.html',
  styleUrls: ['./sustainability-list.component.css']
})
export class SustainabilityListComponent implements OnInit {
  actions: SustainabilityAction[] = [];
  newAction: SustainabilityAction = {
    action: '',
    date: '',
    points: 0
  };

  constructor(private sustainabilityService: SustainabilityService) { }

  ngOnInit(): void {
    this.loadActions();
  }

  loadActions(): void {
    this.sustainabilityService.getActions()
      .subscribe(actions => this.actions = actions);
  }

  onSubmit(): void {
    this.sustainabilityService.addAction(this.newAction)
      .subscribe({
        next: () => {
          this.loadActions();
          this.resetForm();
        },
        error: (error) => console.error('Error adding action:', error)
      });
  }

  private resetForm(): void {
    this.newAction = {
      action: '',
      date: '',
      points: 0
    };
  }
}